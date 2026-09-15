# 🔍 EZ-OSINT Framework v2.0

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Category](https://img.shields.io/badge/Category-Ethical%20Hacking%20%26%20OSINT-red.svg)

**EZ-OSINT Framework** is a lightweight, all-in-one, beginner-friendly Open Source Intelligence (OSINT) reconnaissance tool written in Python. Designed with an intuitive terminal UI (`rich`), it enables ethical hackers, bug bounty hunters, and security researchers to gather public intelligence effortlessly across multiple target vectors.

---

## 🌟 Modules & Features

### 1. 👤 Digital Identity & People Search
* **Phone Number Inspection:** Validates phone structure, carrier provider, line type (mobile/landline), and registered country.
* **Username Finder:** Scans active profile presence across major platforms including GitHub, Twitter/X, Instagram, Reddit, Pinterest, and Telegram.

### 2. 🌐 Network & Infrastructure Reconnaissance
* **IP Geolocation & ISP Lookup:** Resolves domains to IP addresses, geolocation data, ASN, and Internet Service Provider (ISP) information.
* **DNS & Mail Records:** Queries active Mail Exchange (`MX`) records for target domains.

### 3. 🖼️ Imagery & Geospatial Intelligence
* **EXIF Metadata Extractor:** Reads and extracts hidden EXIF metadata from uploaded images (Camera model, timestamp, image dimensions, and capture settings).

### 4. 🔓 Source Code & Leaked Data Detection
* **Public Breach Scanner:** Queries public data breach databases to check if a target email address was involved in known internet leaks.

---

## 💻 Operating System Compatibility

EZ-OSINT Framework is tested and fully compatible with:
* 🪟 **Windows** (CMD & PowerShell)
* 🐧 **Linux Distributions** (Ubuntu, Debian, Fedora, Arch)
* 🐉 **Penetration Testing OS** (Kali Linux, Parrot Security OS)
* 🐧 **WSL** (Windows Subsystem for Linux)
* 📱 **Android Termux**

---

## 🛠️ Installation & Setup

### 1️⃣ Linux / Kali / Parrot / WSL Ubuntu
Open your terminal and run:

```bash
# Update repository packages
sudo apt update && sudo apt upgrade -y

# Install Python3 and Git if not already installed
sudo apt install python3 python3-pip git -y

# Clone this repository
git clone [https://github.com/YOUR_USERNAME/EZ-OSINT-Framework.git](https://github.com/YOUR_USERNAME/EZ-OSINT-Framework.git)
cd EZ-OSINT-Framework

# Install Python dependencies
pip3 install -r requirements.txt

# Run the tool
python3 ultimate_osint.py
