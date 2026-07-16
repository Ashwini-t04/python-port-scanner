from colorama import init, Fore, Style
import socket
import sys
import threading
import argparse
from datetime import datetime
from services import services
from banner import grab_banner
from exporter import export_csv, export_json, export_report
init(autoreset=True)
lock = threading.Lock()
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
            print(
                Fore.GREEN + Style.BRIGHT +
                f"[OPEN] Port {port:<5} ({service})"
            )
            if banner != "No Banner":
                print(
                    Fore.WHITE +
                    f"       Banner: {banner}"
                )
        sock.close()
        return True
    sock.close()
    return False
def scan(target, start_port, end_port):
    start_time = datetime.now()
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "        PYTHON NETWORK PORT SCANNER")
    print(Fore.CYAN + "=" * 60)

    print(Fore.YELLOW + f"Target       : {target}")
    print(Fore.YELLOW + f"Started      : {start_time}")

    print(Fore.CYAN + "=" * 60)
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
        end_time = datetime.now()
        duration = end_time - start_time
        print()
        print(Fore.CYAN + "=" * 60)
        print(Fore.GREEN + Style.BRIGHT + "✓ Scan Completed Successfully")
        print(Fore.CYAN + "=" * 60)

        print(Fore.YELLOW + f"Finished     : {end_time}")
        print(Fore.YELLOW + f"Duration     : {duration}")
        print(Fore.YELLOW + f"Open Ports   : {open_ports}")

        print(Fore.CYAN + "=" * 60)
        export_csv(scan_results)
        export_json(scan_results)
        export_report(
            target,
            target_ip,
            start_port,
            end_port,
            start_time,
            end_time,
            duration,
            scan_results
        )
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
