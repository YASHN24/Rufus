import json
import csv
from typing import Dict

class ContentSynthesizer:

    def filter_relevant_content(self, data, prompt):

        keywords = prompt.lower().split()  # Naive keyword matching
        filtered_data = {
            url: content for url, content in data.items()
            if any(keyword in content.lower() for keyword in keywords)
        }
        return filtered_data


    def synthesize_to_json(self, data: Dict[str, str], output_path: str):

        try:
            with open(output_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Data successfully written to {output_path}")
        except Exception as e:
            print(f"Error writing JSON: {e}")

        pass

    def synthesize_to_csv(self, data: Dict[str, str], output_path: str):

        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["URL", "Content"])
                for url, content in data.items():
                    writer.writerow([url, content[:500]])  # Limit content length for CSV
            print(f"Data successfully written to {output_path}")
        except Exception as e:
            print(f"Error writing CSV: {e}")

        pass
