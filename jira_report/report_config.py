import json
from dataclasses import dataclass
from typing import List


@dataclass
class ReportConfig:
    jql: str
    fields: List[str]
    google_sheet: str
    google_sheet_name: str

    @staticmethod
    def from_json(file_path: str) -> 'ReportConfig':
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                # If fields is not provided in JSON, set a default empty list
                if 'fields' not in data:
                    data['fields'] = []

                return ReportConfig(**data)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"The configuration file {file_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {file_path} contains invalid JSON.")
