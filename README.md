# ⚡ BOLT File Transfer

A lightning-fast, local file transfer web application built with Flask and modern web technologies. Transfer files between devices on the same network with a simple 4-digit code.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **📁 File & Folder Transfer**: Support for both individual files and entire directories
- **⚡ Lightning Fast**: Local network transfers for maximum speed
- **🎨 Modern UI**: Dark theme with responsive design and drag-and-drop functionality
- **🔢 Simple Code System**: 4-digit codes for easy sharing
- **📊 Progress Tracking**: Real-time upload progress with speed and ETA estimates
- **🕒 Auto-Cleanup**: Files automatically removed after 5 minutes
- **📱 Mobile Friendly**: Works seamlessly on desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/bolt-file-transfer.git
   cd bolt-file-transfer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask werkzeug
   ```

### Running the Application

1. **Start the server**
   ```bash
   python app.py
   ```

2. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

3. **Share the application**
   Other devices on the same network can access it using your computer's IP address:
   `http://[YOUR-IP-ADDRESS]:8000`

## 🎯 How to Use

### Sending Files

1. Click the **"Send"** button
2. Choose between File or Folder transfer
3. Drag and drop files or click to select
4. Click **"Start Upload"**
5. Share the 4-digit code with the recipient

### Receiving Files

1. Click the **"Receive"** button
2. Enter the 4-digit code provided by the sender
3. Click **"Show Files"**
4. Download individual files or **"Download All"**

## 🏗️ Project Structure

```
bolt/
├── app.py           # Flask backend server
├── templates/
 ├── index.html          # Frontend interface
├── uploads/            # Directory for temporary file storage
└── README.md           # Project documentation
```

## 🔧 Technical Details

### Backend (Flask)
- Handles file uploads/downloads with chunked transfer
- Generates unique 4-digit codes for each transfer
- Manages temporary file storage with auto-cleanup
- Provides RESTful API for frontend communication

### Frontend (HTML/CSS/JS)
- Responsive design with Tailwind CSS
- Drag-and-drop file interface
- Real-time progress updates
- Modern UI with dark theme

### Security Features
- File name sanitization
- Temporary file storage (auto-deletion)
- No persistent data storage
- Local network only by default

## 🌟 Future Enhancements

- [ ] WebRTC integration for direct P2P transfers
- [ ] QR code generation for easier code sharing
- [ ] Transfer history and analytics
- [ ] Customizable expiration times
- [ ] Password-protected transfers
- [ ] Mobile app version

## 🤝 Contributing



## 🛠️ Development

### Running in Development Mode
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

### Debug Mode
For troubleshooting, enable debug mode in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
```

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact us at murugesapandiyan34@gmail.com

