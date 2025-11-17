# SecuShield Antivirus

SecuShield est un antivirus basique conçu pour détecter et gérer les menaces en fonction d'une base de signatures.

## Fonctionnalités
- Scan de fichiers
- Gestion de la quarantaine
- Génération de rapports
- Interface utilisateur simple

## Utilisation
1. Lancez `src/main.py` pour démarrer l'application.
2. Naviguez dans l'interface pour utiliser les différentes fonctionnalités.

## Dépendances
- Python 3.x
- Tkinter

## Structure du Projet

🚀 Features
🔍 File, Folder & System Scanning

Fast multi-threaded scanning

Recursive folder analysis

Real-time progress display (current file, time estimation)

Detection actions: Delete, Quarantine, Ignore


cahier des charges

🧠 Threat Detection Engine

500,000+ local MD5 signatures

VirusTotal API integration (70+ antivirus engines)

Hash checking + automatic file upload for unknown samples

Detailed and secure logging


cahier des charges

🔒 Advanced Quarantine System

Secure isolated directory

File metadata preservation

One-click restore or permanent deletion

Dedicated GUI management panel


cahier des charges

📊 Dashboard & Real-Time Statistics

Global threat metrics

Total scans, detections, quarantined items

Disk usage & system info

Quick actions panel


cahier des charges

📈 Interactive Statistics & Graphs

Threat evolution timeline

Scan history & activity charts

File-type breakdown

Flexible time filtering (7 days, 30 days, yearly…)


cahier des charges

📝 Multi-Format Reports

HTML (professional with CSS styling)

JSON

Plain TXT

Includes system info, scan results, timestamps, actions taken


cahier des charges

📘 Built-in Security Guide

50+ practical cybersecurity tips

Organized by themes (Internet safety, emergencies, advanced protection…)

Accessible directly within the app


cahier des charges

🎨 Modern User Interface

PyQt5 Material Design style

Light & dark themes

Smooth animations and ergonomic navigation


cahier des charges

🧩 Tech Stack

Python 3.8+

PyQt5 (GUI)

Requests (API calls)

Psutil (system information)

Hashlib (MD5/SHA256)

Threading module


cahier des charges

🗂 Project Structure
SecuShield/
├── src/
│   ├── gui/
│   ├── utils/
├── data/
│   ├── quarantine/
│   └── reports/
├── database/
│   └── Hashes.txt
└── main.py


cahier des charges

🎯 Objectives & Success Criteria

Fast scanning (<100ms for small files)

Lightweight (<200MB RAM)

Fully responsive UI (no freezing)

Accurate detections:

100% known viruses (local DB)

95%+ via VirusTotal

Zero-crash stability in normal use


cahier des charges

🛣 Future Improvements

Real-time protection (file system monitoring)

Automatic updates

Machine learning detection

Sandbox analysis

REST API for enterprise environments
