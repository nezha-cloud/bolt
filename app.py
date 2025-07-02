from flask import Flask, request, send_from_directory, render_template, jsonify, send_file, abort
import os
import io
import zipfile

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Increase max upload size to 1GB (adjust as needed)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 * 1024  * 1024

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    code = request.form.get('code')
    relative_path = request.form.get('relative_path')  # New: folder structure from client
    if not file or not code:
        return jsonify({'success': False, 'error': 'No file or code provided'}), 400
    code_folder = os.path.join(app.config['UPLOAD_FOLDER'], code)
    os.makedirs(code_folder, exist_ok=True)
    # Save file with folder structure if provided
    if relative_path:
        save_path = os.path.join(code_folder, relative_path)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        file.save(save_path)
        saved_name = relative_path
    else:
        save_path = os.path.join(code_folder, file.filename)
        file.save(save_path)
        saved_name = file.filename
    return jsonify({'success': True, 'filename': saved_name})

@app.route('/download/<code>/<filename>')
def download(code, filename):
    code_folder = os.path.join(app.config['UPLOAD_FOLDER'], code)
    return send_from_directory(code_folder, filename, as_attachment=True)

@app.route('/download_zip/<code>')
def download_zip(code):
    code_folder = os.path.join(app.config['UPLOAD_FOLDER'], code)
    if not os.path.exists(code_folder):
        abort(404)
    # Recursively collect all files with their relative paths
    files = []
    for root, dirs, filenames in os.walk(code_folder):
        for f in filenames:
            rel_path = os.path.relpath(os.path.join(root, f), code_folder)
            files.append(rel_path)
    if not files:
        abort(404)
    mem_zip = io.BytesIO()
    with zipfile.ZipFile(mem_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for rel_path in files:
            abs_path = os.path.join(code_folder, rel_path)
            zf.write(abs_path, arcname=rel_path)
    mem_zip.seek(0)
    return send_file(mem_zip, mimetype='application/zip', as_attachment=True, download_name=f'{code}_files.zip')

@app.route('/autodownload')
def autodownload():
    code = request.args.get('code')
    if not code:
        return jsonify({'success': False, 'error': 'No code provided'}), 400
    code_folder = os.path.join(app.config['UPLOAD_FOLDER'], code)
    if not os.path.exists(code_folder):
        return jsonify({'success': False, 'error': 'No files available'}), 404

    # Recursively list all files with relative paths
    files = []
    for root, dirs, filenames in os.walk(code_folder):
        for f in filenames:
            rel_path = os.path.relpath(os.path.join(root, f), code_folder)
            files.append(rel_path.replace("\\", "/"))  # Use forward slashes for URLs

    if not files:
        return jsonify({'success': False, 'error': 'No files available'}), 404
    return jsonify({'success': True, 'files': files})

if __name__ == '__main__':
    # Enable threading for concurrent uploads (development only)
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
