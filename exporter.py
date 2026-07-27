from pathlib import Path
import csv
import json
from colorama import Fore, Style

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def export_csv(scan_results):
    csv_path = OUTPUT_DIR / "scan_results.csv"

    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Port", "Service", "Banner"])

        for result in scan_results:
            writer.writerow([
                result["port"],
                result["service"],
                result["banner"]
            ])

    print(Fore.GREEN + Style.BRIGHT +
      f"✓ Results saved to {csv_path}")

def export_json(scan_results):
    json_path = OUTPUT_DIR / "scan_results.json"
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(scan_results, file, indent=4)

    print(Fore.GREEN + Style.BRIGHT +
          f"✓ Results saved to {json_path}")

def export_report(target, target_ip, start_port, end_port,
                  start_time, end_time, duration, scan_results):

    report_path = OUTPUT_DIR / "scan_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:

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
      f"✓ Results saved to {report_path}")