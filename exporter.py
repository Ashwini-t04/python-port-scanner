import os
import csv
import json

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

    print("Results saved to output/scan_results.csv")

os.makedirs("output", exist_ok=True)
def export_json(scan_results):
    with open("output/scan_results.json", "w") as file:
        json.dump(scan_results, file, indent=4)

    print("Results saved to output/scan_results.json")