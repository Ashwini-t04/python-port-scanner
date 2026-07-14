import socket
import sys
import csv
from datetime import datetime
services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}
def scan(target, start_port, end_port):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Time Started: {datetime.now()}")
    print("-" * 50)
    try:
        # Convert the domain name into an IP address
        target_ip = socket.gethostbyname(target)
        open_ports = 0
        scan_results = []
        # Scan every port in the specified range
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports += 1
                service = services.get(port, "Unknown Service")
                scan_results.append({"port": port, "service": service})
                print(f"[OPEN] Port {port} ({service})")
        print("-" * 50)
        print("Scan Completed")
        print(f"Total Open Ports: {open_ports}")
        with open("scan_results.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Port", "Service"])
            for result in scan_results:
                writer.writerow([result["port"], result["service"]])
        print("Results saved to scan_results.csv")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Couldn't connect to server.")
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
        sys.exit() 
if __name__ == "__main__":
    target = input("Enter Target IP or Domain: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))
    scan(target, start_port, end_port)


