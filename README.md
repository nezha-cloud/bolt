⚡ BOLT File Transfer

A lightning-fast local file transfer web application built with **Flask** and modern web technologies.  
Transfer files and folders between devices on the same network using a simple **4-digit code**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 📁 **File & Folder Transfer** – Supports individual files and entire directories  
- ⚡ **High-Speed Local Transfers** – Optimized for LAN usage  
- 🎨 **Modern UI** – Dark theme, responsive design, drag & drop support  
- 🔢 **Simple Code System** – Temporary 4-digit sharing codes  
- 📊 **Progress Tracking** – Real-time upload speed and ETA  
- 🕒 **Auto Cleanup** – Files are automatically deleted after transfer  
- 📱 **Mobile Friendly** – Works on desktop and mobile browsers  

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8 or higher**
- pip (Python package manager)

---

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/bolt-file-transfer.git
   cd bolt-file-transfer
Create a virtual environment (recommended)



python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
Install dependencies


pip install -r requirements.txt
▶️ Running the Application
Start the server



python app.py
Access in browser



http://localhost:8000
Access from other devices (same network)



http://<YOUR-IP-ADDRESS>:8000
🎯 How to Use
Sending Files
Click Send

Select File or Folder

Drag & drop files or click to select

Click Start Upload

Share the generated 4-digit code

Receiving Files
Click Receive

Enter the 4-digit code

Click Show Files

Download individual files or Download All

🏗️ Project Structure
bash
Copy code
bolt/
├── app.py                # Flask backend server
├── templates/
│   └── index.html        # Frontend interface
├── uploads/              # Temporary file storage
├── screenshots/          # Demo images
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── LICENSE

🔧 Technical Details
Backend (Flask)
Handles file uploads and downloads

Generates unique 4-digit transfer codes

Manages temporary file storage

Automatic cleanup after transfer completion

Frontend (HTML / CSS / JS)
Built using Tailwind CSS

Drag & drop file handling

Real-time progress updates

Dark-themed, responsive UI

🔐 Security Notes
Temporary file storage only

File names are sanitized

No persistent database

Intended for local network usage

🌟 Future Enhancements
WebRTC-based peer-to-peer transfer

QR code support for faster pairing

Transfer history

Custom expiration time

Password-protected transfers

Docker support

🤝 Contributing
Contributions are welcome.

Fork the repository

Create a new branch 

Commit your changes

Open a Pull Request

📬 Contact
📧 Email: murugesapandiyan34@gmail.com