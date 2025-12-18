# BOLT File Transfer

A lightning-fast local file transfer web application built with Flask and modern web technologies. Transfer files and folders between devices on the same network using a simple 4-digit code.

## ✨ Features

- **📁 File & Folder Transfer** – Supports individual files and entire directories
- **⚡ High-Speed Local Transfers** – Optimized for LAN usage
- **🎨 Modern UI** – Dark theme, responsive design, drag & drop support
- **🔢 Simple Code System** – Temporary 4-digit sharing codes
- **📊 Progress Tracking** – Real-time upload speed and ETA
- **🕒 Auto Cleanup** – Files are automatically deleted after transfer
- **📱 Mobile Friendly** – Works on desktop and mobile browsers

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/bolt-file-transfer.git
cd bolt-file-transfer
```

2. Create a virtual environment (recommended)
```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

1. Start the server
```bash
python app.py
```

2. Access in browser
```
http://localhost:8000
```

3. Access from other devices (same network)
```
http://<your-ip-address>:8000
```

## 🎯 How to Use

### Sending Files
1. Click **Send**
2. **Select File or Folder**
   - Drag & drop files or click to select
3. Click **Start Upload**
4. Share the generated **4-digit code**

### Receiving Files
1. Click **Receive**
2. Enter the **4-digit code**
3. Click **Show Files**
4. **Download individual files** or **Download All**

## 🏗️ Project Structure
```
bolt/
├── app.py              # Flask backend server
├── templates/
│   └── index.html     # Frontend interface
├── uploads/           # Temporary file storage
├── screenshots/       # Demo images
├── requirements.txt   # Dependencies
├── README.md          # Documentation
└── LICENSE
```

## 🔧 Technical Details

### Backend (Flask)
- Handles file uploads and downloads
- Generates unique 4-digit transfer codes
- Manages temporary file storage
- Automatic cleanup after transfer completion

### Frontend (HTML / CSS / JS)
- Built using Tailwind CSS
- Drag & drop file handling
- Real-time progress updates
- Dark-themed, responsive UI

## 🔐 Security Notes
- Temporary file storage only
- File names are sanitized
- No persistent database
- Intended for local network usage

## 🌟 Future Enhancements
- WebRTC-based peer-to-peer transfer
- QR code support for faster pairing
- Transfer history
- Custom expiration time
- Password-protected transfers
- Docker support

## 🤝 Contributing
Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

## 📬 Contact
**📧 Email:** murugesapandiyan34@gmail.com
