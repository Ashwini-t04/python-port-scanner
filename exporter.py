import os
import csv
import json
from colorama import Fore, Style
os.makedirs("output", exist_ok=True)
def export_csv(scan_results):
    with open("output/scan_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Service", "Banner"])

        for result in scan_results:
            writer.writerow([
                result["port"],
                result["service"],
                result["banner"]
            ])

    print(Fore.GREEN + Style.BRIGHT +
      "✓ Results saved to output/scan_results.csv")

os.makedirs("output", exist_ok=True)
def export_json(scan_results):
    with open("output/scan_results.json", "w") as file:
        json.dump(scan_results, file, indent=4)

    print(Fore.GREEN + Style.BRIGHT +
      "✓ Results saved to output/scan_results.json")

def export_report(target, target_ip, start_port, end_port,
                  start_time, end_time, duration, scan_results):

    import os

    os.makedirs("output", exist_ok=True)

    report_path = "output/scan_report.txt"

    with open(report_path, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("        PYTHON NETWORK PORT SCANNER REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Target          : {target}\n")
        file.write(f"Resolved IP     : {target_ip}\n")
        file.write(f"Scan Started    : {start_time}\n")
        file.write(f"Scan Finished   : {end_time}\n")
        file.write(f"Duration        : {duration}\n")
        file.write(f"Port Range      : {start_port}-{end_port}\n\n")

        file.write("-" * 60 + "\n")
        file.write("OPEN PORTS\n")
        file.write("-" * 60 + "\n")

        for result in scan_results:
            file.write(f"\nPort    : {result['port']}\n")
            file.write(f"Service : {result['service']}\n")
            file.write(f"Banner  : {result['banner']}\n")

        file.write("\n" + "-" * 60 + "\n")
        file.write("SUMMARY\n")
        file.write("-" * 60 + "\n")

        total_ports = end_port - start_port + 1

        file.write(f"Ports Scanned : {total_ports}\n")
        file.write(f"Open Ports    : {len(scan_results)}\n")
        file.write(f"Closed Ports  : {total_ports - len(scan_results)}\n")

    print(Fore.GREEN + Style.BRIGHT +
      "✓ Results saved to output/scan_report.txt")