import json
from dataclasses import dataclass


@dataclass
class ReportConfig:
    jql: str
    google_sheet: str
    google_sheet_name: str

    @staticmethod
    def from_json(file_path: str) -> 'ReportConfig':
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return ReportConfig(**data)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The configuration file {file_path} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"The file {file_path} contains invalid JSON.")
