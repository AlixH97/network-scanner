# 🔍 Network Scanner Tool

A Python-based network scanning tool that detects live hosts, open ports, and running services across a network range. Built to demonstrate practical networking and cybersecurity skills.

---

## 📌 Features

- Scans single IPs or entire network ranges (e.g. `192.168.1.0/24`)
- Detects live hosts and their hostnames
- Identifies open ports and running services with version detection
- Saves results to a timestamped JSON report
- Clean, readable terminal output

---

## 🛠️ Tech Stack

- **Python 3**
- **python-nmap** — Python wrapper for Nmap
- **Nmap** — Network scanning engine

---

## ⚙️ Installation

### 1. Install Nmap

**macOS:**
```bash
brew install nmap
```

**Linux (Ubuntu/Kali):**
```bash
sudo apt-get install nmap
```

### 2. Clone the repository
```bash
git clone https://github.com/AlixH97/network-scanner.git
cd network-scanner
```

### 3. Install Python dependencies
```bash
pip3 install -r requirements.txt
```

---

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

---

## 📄 Example Output
============================================================
🔍 NETWORK SCANNER - Starting Scan
Target  : 192.168.1.0/24
Ports   : 22,80,443,3389,8080
Time    : 2026-04-24 14:30:00
──────────────────────────────────────────────────
🖥️  Host     : 192.168.1.1
📛 Hostname : router.local
✅ Status   : UP
📡 Open Ports:
Port 80/tcp   →  HTTP         Apache httpd 2.4.41
Port 443/tcp  →  HTTPS        OpenSSL 1.1.1
💾 Report saved to: scan_report_20260424_143000.json
---

## 📁 Project Structure
---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **authorized network scanning only**.
Always ensure you have permission before scanning any network or device.
Unauthorized scanning may be illegal in your jurisdiction.

---

## 👤 Author

**Ali Hussnain**
MSc IT Security Management — Arden University Berlin
CCNA Certified | Network & Security Professional
📧 alihussnain8808@gmail.com
📍 Berlin, Germany

---

## 📜 License

MIT License — feel free to use and modify with attribution.
