import socket
import sys
import csv
import json
import threading
import argparse
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
lock = threading.Lock()
def grab_banner(sock, port):
    try:
        if port == 80:
            sock.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

        banner = sock.recv(1024).decode(errors="ignore").strip()

        return banner

    except:
        return "No Banner"
def scan_port(target_ip, port, scan_results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        service = services.get(port, "Unknown Service")
        banner = grab_banner(sock, port)
        with lock:
            scan_results.append({
                "port": port,
                "service": service,
                "banner": banner
            })
            print(f"[OPEN] Port {port} ({service})")
            if banner != "No Banner":
                print(f"       Banner: {banner}")
        sock.close()
        return True
    sock.close()
    return False
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
        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(
                target=scan_port,
                args=(target_ip, port, scan_results)
            )
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        open_ports = len(scan_results)
        print("-" * 50)
        print("Scan Completed")
        print(f"Total Open Ports: {open_ports}")
        with open("scan_results.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Port", "Service"])
            for result in scan_results:
                writer.writerow([result["port"], result["service"]])
        print("Results saved to scan_results.csv")
        with open("scan_results.json", "w") as file:
            json.dump(scan_results, file, indent=4)
        print("Results saved to scan_results.json")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Couldn't connect to server.")
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
        sys.exit() 
parser = argparse.ArgumentParser(description="Python Network Port Scanner")

parser.add_argument("target", help="Target IP address or domain")
parser.add_argument("start_port", type=int, help="Starting port")
parser.add_argument("end_port", type=int, help="Ending port")

args = parser.parse_args()
if __name__ == "__main__":
    scan(args.target, args.start_port, args.end_port)
