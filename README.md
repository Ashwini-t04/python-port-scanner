# Python Network Port Scanner
## Description
This is a Python-based TCP Port Scanner that scans a user-specified range of ports on a target IP address or domain name. The application identifies open and closed ports, handles common network errors gracefully, and displays the total number of open ports after the scan. This project was built to learn Python socket programming, TCP/IP networking, and basic cybersecurity concepts.
## Features
- Scan a target using an IP address or domain name.
- Scan a user-defined range of TCP ports.
- Display open ports.
- Count and display the total number of open ports.
- Handle invalid hostnames and network errors gracefully.
- Allow users to stop the scan safely using `Ctrl + C`.
## Technologies Used
- Python 3
- Socket Module
- TCP/IP Networking
- Datetime Module
- Sys Module
## How It Works
1. The user enters a target IP address or domain name.
2. The user specifies the starting and ending port numbers to scan.
3. The program resolves the domain name into its corresponding IP address.
4. It creates a TCP socket and attempts to connect to each port within the specified range.
5. If the connection is successful, the port is displayed as **OPEN**.
6. After checking each port, the socket is closed before moving to the next port.
7. Once all ports have been scanned, the program displays the total number of open ports found.
8. The program also handles invalid hostnames, network errors, and user interruptions gracefully.
## Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Ensure Python 3 is installed on your system.
4. Run the application using Python.
## How to Run
```bash
python scanner.py
```
When prompted, enter:
- Target IP address or domain name
- Starting port number
- Ending port number
## Example Output

```text
--------------------------------------------------
Scanning Target: scanme.nmap.org
Time Started: 2026-07-14 14:30:15
--------------------------------------------------

[OPEN] Port 22
...
[OPEN] Port 80

--------------------------------------------------
Scan Completed
Total Open Ports: 2
--------------------------------------------------
```
## Project Structure

```text
Python-Port-Scanner/
│
├── scanner.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── screenshots/
    └── scan_result.png
```
## Future Improvements

- Add service detection for open ports.
- Export scan results to CSV and JSON formats.
- Implement multithreading for faster scanning.
- Support command-line arguments using `argparse`.
- Improve the user interface with colored terminal output.
- Display the total scan duration.
## Disclaimer

This project is intended for educational purposes only. Use this tool only on systems and networks that you own or have explicit permission to test. Unauthorized network scanning may violate laws or organizational policies.