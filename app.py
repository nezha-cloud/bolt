from flask import Flask, render_template, request, jsonify, send_from_directory, after_this_request
from werkzeug.utils import secure_filename
import os
import shutil
import random
import string
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 * 1024  # 1TB

# Simulated upload speed in MB/s (adjust based on your server/network)
UPLOAD_SPEED_MBPS = 50

active_codes = {}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def generate_code():
    """Generates a unique 4-digit numeric code."""
    while True:
        code = ''.join(random.choices(string.digits, k=4))
        if code not in active_codes:
            return code

def estimate_upload_time(total_bytes):
    """Returns estimated upload time in seconds based on simulated speed."""
    total_mb = total_bytes / (1024 * 1024)
    return round(total_mb / UPLOAD_SPEED_MBPS, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('file')
    relative_paths = request.form.getlist('relative_paths')

    if not files:
        return jsonify({'success': False, 'error': 'No files selected.'}), 400

    code = generate_code()
    upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], code)
    os.makedirs(upload_dir, exist_ok=True)

    uploaded_files_data = []
    total_size = 0

    for i, f in enumerate(files):
        if f.filename:
            file_bytes = f.read()
            total_size += len(file_bytes)
            f.stream.seek(0)  # Reset stream after reading

            if relative_paths and i < len(relative_paths):
                full_path = os.path.join(upload_dir, relative_paths[i])
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                f.save(full_path)
                uploaded_files_data.append(relative_paths[i])
            else:
                filename = secure_filename(f.filename)
                file_path = os.path.join(upload_dir, filename)
                f.save(file_path)
                uploaded_files_data.append(filename)

    if not uploaded_files_data:
        return jsonify({'success': False, 'error': 'No files uploaded.'}), 400

    active_codes[code] = uploaded_files_data
    eta = estimate_upload_time(total_size)

    return jsonify({
        'success': True,
        'code': code,
        'files_uploaded': uploaded_files_data,
        'estimated_upload_time_sec': eta,
        'message': f'Upload complete. Estimated time: {eta} seconds.'
    })

@app.route('/list_files')
def list_files():
    code = request.args.get('code')
    files = active_codes.get(code)

    if not files:
        return jsonify({'success': False, 'error': 'Invalid or expired code.'}), 404

    return jsonify({'success': True, 'files': files, 'message': 'Files listed successfully.'})

@app.route('/download/<code_id>/<path:filename>')
def download_file(code_id, filename):
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], code_id)

    @after_this_request
    def cleanup(response):
        try:
            download_count = request.args.get('download_count', 0, type=int)
            total_files = len(active_codes.get(code_id, []))
            if download_count >= total_files:
                shutil.rmtree(folder_path)
                active_codes.pop(code_id, None)
        except Exception as e:
            print(f"Cleanup error: {e}")
        return response

    return send_from_directory(folder_path, secure_filename(filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)