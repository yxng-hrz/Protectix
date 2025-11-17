# 🛡️ SecuShield — Modern Antivirus with GUI
*A next-generation antivirus built with Python & PyQt5*

## 📌 Overview
SecuShield is a modern, full-featured antivirus designed to provide efficient malware detection, an intuitive user interface, and a rich set of protection tools.  
It integrates **local signature-based scanning**, **VirusTotal cloud analysis**, a **quarantine system**, **detailed reporting**, and **interactive security guidance**.

This project aims to combine **strong security**, **performance**, and **educational value**, offering a user-friendly application that rivals commercial antivirus solutions.

---

## 🚀 Features

### 🔍 File, Folder & System Scanning
- Fast multi-threaded scanning  
- Recursive folder analysis  
- Real-time progress display (current file, time estimation)  
- Detection actions: *Delete*, *Quarantine*, *Ignore*

### 🧠 Threat Detection Engine
- 500,000+ local MD5 signatures  
- VirusTotal API integration (70+ antivirus engines)  
- Hash checking + automatic file upload for unknown samples  
- Detailed and secure logging  

### 🔒 Advanced Quarantine System
- Secure isolated directory  
- File metadata preservation  
- One-click restore or permanent deletion  
- Dedicated GUI management panel  

### 📊 Dashboard & Real-Time Statistics
- Global threat metrics  
- Total scans, detections, quarantined items  
- Disk usage & system info  
- Quick actions panel  

### 📈 Interactive Statistics & Graphs
- Threat evolution timeline  
- Scan history & activity charts  
- File-type breakdown  
- Flexible time filtering (7 days, 30 days, yearly…)  

### 📝 Multi-Format Reports
- HTML (professional with CSS styling)  
- JSON  
- Plain TXT  
- Includes system info, scan results, timestamps, actions taken  

### 📘 Built-in Security Guide
- 50+ practical cybersecurity tips  
- Organized by themes (Internet safety, emergencies, advanced protection…)  
- Accessible directly within the app  

### 🎨 Modern User Interface
- PyQt5 Material Design style  
- Light & dark themes  
- Smooth animations and ergonomic navigation  

---

## 🧩 Tech Stack
- **Python 3.8+**  
- **PyQt5** (GUI)  
- **Requests** (API calls)  
- **Psutil** (system information)  
- **Hashlib** (MD5/SHA256)  
- **Threading** module  

---

## 🗂 Project Structure
SecuShield/
├── src/
│ ├── gui/
│ │ ├── main_gui.py
│ │ ├── dashboard_section.py
│ │ ├── scan_section.py
│ │ ├── quarantine_section.py
│ │ ├── reports_section.py
│ │ ├── stats_viewer.py
│ │ ├── guide_section.py
│ │ ├── theme_switcher.py
│ │ └── decision_helper.py
│ └── utils/
│ ├── file_scanner.py
│ ├── quarantine_manager.py
│ ├── report_generator.py
│ └── virustotal_scanner.py
├── data/
│ ├── quarantine/
│ └── reports/
├── database/
│ └── Hashes.txt
└── main.py



---

## 🎯 Objectives & Success Criteria
- Fast scanning (<100ms for small files)  
- Lightweight (<200MB RAM)  
- Fully responsive UI (no freezing)  
- Accurate detections:  
  - 100% known viruses (local DB)  
  - 95%+ via VirusTotal  
- Zero-crash stability in normal use  

---

## 🛣 Future Improvements
- Real-time protection (file system monitoring)  
- Automatic updates  
- Machine learning detection  
- Sandbox analysis  
- REST API for enterprise environments  
- macOS support  

---
