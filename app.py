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
    """Generates a unique 4-digit numeric code more efficiently."""
    existing_codes = set(active_codes.keys())
    for _ in range(100):  # Limit attempts
        code = ''.join(random.choices(string.digits, k=4))
        if code not in existing_codes:
            return code
    # Fallback: use timestamp-based code if too many collisions
    return str(int(time.time()))[-4:].zfill(4)

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

    # COMBINED PASS: Calculate size and save files simultaneously
    for i, f in enumerate(files):
        if f.filename:
            # Get file size from content length if available (more efficient)
            file_size = f.content_length
            if file_size is None:
                # Fallback to seeking method only if needed
                current_pos = f.tell()
                f.seek(0, 2)
                file_size = f.tell()
                f.seek(current_pos)
            
            total_size += file_size

            # Save file immediately after size calculation
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

    active_codes[code] = {
        'files': uploaded_files_data,
        'upload_dir': upload_dir
    }
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
    code_data = active_codes.get(code)
    
    if not code_data:
        return jsonify({'success': False, 'error': 'Invalid or expired code.'}), 404

    files = code_data['files']
    return jsonify({'success': True, 'files': files, 'message': 'Files listed successfully.'})

@app.route('/download/<code_id>')
@app.route('/download/<code_id>/<path:filename>')
def download_file(code_id, filename=None):
    code_data = active_codes.get(code_id)
    
    if not code_data:
        return jsonify({'success': False, 'error': 'Invalid or expired code.'}), 404
    
    folder_path = code_data['upload_dir']
    
    if filename is None:
        # Return list of files if no filename provided
        files = code_data['files']
        return jsonify({'success': True, 'files': files})
    
    # Ensure the file exists
    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'error': 'File not found.'}), 404

    @after_this_request
    def cleanup(response):
        try:
            # Check if this was the last file to download
            download_count = request.args.get('download_count', 0, type=int)
            total_files = len(code_data['files'])
            if download_count >= total_files:
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                active_codes.pop(code_id, None)
                print(f"Cleaned up files for code: {code_id}")
        except Exception as e:
            print(f"Cleanup error: {e}")
        return response

    try:
        return send_from_directory(
            folder_path, 
            filename, 
            as_attachment=True,
            download_name=os.path.basename(filename)  # Set proper download name
        )
    except Exception as e:
        return jsonify({'success': False, 'error': f'Download failed: {str(e)}'}), 500

@app.route('/cleanup')
def cleanup():
    code = request.args.get('code')
    if not code:
        return jsonify({'success': False, 'error': 'No code provided.'}), 400
    
    code_data = active_codes.get(code)
    if not code_data:
        return jsonify({'success': False, 'error': 'Invalid code.'}), 404
    
    folder_path = code_data['upload_dir']
    
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        active_codes.pop(code, None)
        return jsonify({'success': True, 'message': 'Cleanup successful.'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)