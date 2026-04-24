# 🔍 Network Scanner Tool

A Python-based network scanning tool that detects live hosts, open ports, and running services across a network range. Built to demonstrate practical networking and cybersecurity skills.

## 📌 Features
- Scans single IPs or entire network ranges (e.g. `192.168.1.0/24`)
- Detects live hosts and their hostnames
- Identifies open ports and running services with version detection
- Saves results to a timestamped JSON report
- Clean, readable terminal output

## 🛠️ Tech Stack
- **Python 3**
- **python-nmap** — Python wrapper for Nmap
- **Nmap** — Network scanning engine

## ⚙️ Installation

### 1. Install Nmap
```bash
brew install nmap
```

### 2. Install Python dependencies
```bash
pip3 install python-nmap
```

## 🚀 Usage
```bash
# Scan a single host
python3 scanner.py 192.168.1.1

# Scan a full network range
python3 scanner.py 192.168.1.0/24

# Scan with custom ports
python3 scanner.py 192.168.1.0/24 80,443,22,8080

# Run default demo (scans localhost)
python3 scanner.py
```

## ⚠️ Disclaimer
This tool is intended for **educational purposes** and **authorized network scanning only**. Always ensure you have permission before scanning any network or device.

## 👤 Author
**Ali Hussnain**
MSc IT Security Management — Arden University Berlin
CCNA Certified | Network & Security Professional
📧 alihaider060298@gmail.com
📍 Berlin, Germany

## 📜 License
MIT License
