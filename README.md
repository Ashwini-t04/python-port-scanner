# Python Network Port Scanner
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

A multithreaded TCP port scanner built with Python that performs TCP port scanning, service detection, banner grabbing, and generates professional scan reports in CSV, JSON, and TXT formats.

## Overview

The Python Network Port Scanner is a command-line tool designed to identify open TCP ports on a target system. In addition to detecting open ports, it identifies common services running on those ports, attempts basic banner grabbing, and exports scan results into multiple report formats.

The project is structured using a modular architecture, separating scanning, service detection, banner grabbing, and report generation into independent modules. This improves code readability, maintainability, and scalability.

This project is intended for educational purposes, networking practice, and authorized security assessments.

## 📑 Table of Contents

- Overview
- Features
- Project Structure
- Technologies Used
- Installation
- Usage
- Generated Reports
- Screenshots
- Version History
- Requirements
- Contributing
- License
- Disclaimer
---

## Features

### 🔍 Network Scanning

- TCP Port Scanning
- Scan custom port ranges
- Supports both IP addresses and domain names
- DNS hostname resolution

### 🌐 Service Detection

- Detects common network services
- Maps well-known ports to their corresponding services
- Identifies unknown services when no mapping exists

### 📡 Banner Grabbing

- Attempts to retrieve service banners
- Displays server information when available

### ⚡ Performance

- Multithreaded scanning
- Faster execution through concurrent scanning
- Thread-safe result collection

### 📊 Report Generation

- CSV Export
- JSON Export
- Professional TXT Report

### 💻 Command-Line Interface

Run the scanner directly from the terminal.

Example:

```bash
python scanner.py scanme.nmap.org 1 100
```

### 🏗️ Project Architecture

- Modular Python design
- Separate modules for:
  - Scanning
  - Banner Grabbing
  - Service Detection
  - Report Generation
- Organized project structure
---

## 📂 Project Structure

```text
python-port-scanner/
│
├── scanner.py          # Main application entry point
├── banner.py           # Banner grabbing functionality
├── exporter.py         # Report generation (CSV, JSON, TXT)
├── services.py         # Common service name mappings
│
├── output/
│   ├── scan_results.csv
│   ├── scan_results.json
│   └── scan_report.txt
│
├── screenshots/
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3
- Socket Programming
- Multithreading
- Colorama
- CSV
- JSON
- Git
- GitHub

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ashwini-t04/python-port-scanner.git
```

### 2. Navigate to the project directory

```bash
cd python-port-scanner
```

### 3. Install the required dependency

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the scanner from the command line.

### Syntax

```bash
python scanner.py <target> <start_port> <end_port>
```

### Example

```bash
python scanner.py scanme.nmap.org 1 100
```

### Another Example

```bash
python scanner.py 192.168.1.100 20 1000
```

Replace the IP address or domain name with the target you want to scan.

> **Note:** Only scan systems and networks for which you have explicit authorization.
---

## 📄 Generated Reports

After every successful scan, the scanner automatically generates the following reports inside the `output/` directory.

### 📊 CSV Report

The CSV report is suitable for spreadsheets and data analysis.

It contains:

- Port Number
- Service Name
- Banner Information

Example:

| Port | Service | Banner |
|------|---------|--------|
| 22 | SSH | SSH-2.0-OpenSSH_9.6 |
| 80 | HTTP | HTTP/1.1 200 OK |

---

### 📦 JSON Report

The JSON report stores the scan results in a structured format, making it suitable for automation and integration with other tools.

Example:

```json
[
    {
        "port": 22,
        "service": "SSH",
        "banner": "SSH-2.0-OpenSSH_9.6"
    },
    {
        "port": 80,
        "service": "HTTP",
        "banner": "HTTP/1.1 200 OK"
    }
]
```

---

### 📝 TXT Report

The TXT report provides a human-readable summary of the scan.

It includes:

- Target
- Resolved IP Address
- Scan Start Time
- Scan Finish Time
- Scan Duration
- Port Range
- Open Ports
- Service Names
- Banner Information
- Scan Summary

---

## 📌 Version History

| Version | Features Added |
|----------|----------------|
| **v1.0** | Basic TCP Port Scanner |
| **v2.0** | Service Detection |
| **v3.0** | CSV Report Generation |
| **v4.0** | JSON Report Generation |
| **v5.0** | Multithreaded Port Scanning |
| **v6.0** | Banner Grabbing |
| **v7.0** | Command-Line Interface (CLI) |
| **v8.0** | Modular Project Structure |
| **v9.0** | Professional TXT Report Generation |
| **v10.0** | Enhanced Terminal UI with Colorized Output |

---

## 📝 Requirements

- Python **3.10** or later
- Colorama

Install the required dependency:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## ⚠️ Disclaimer

This tool is intended solely for educational purposes and authorized security assessments.

Only scan systems, networks, or devices for which you have explicit permission. The author is not responsible for any misuse or unauthorized use of this software.