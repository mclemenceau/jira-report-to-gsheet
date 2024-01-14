import pytest
import json
import os
from jira_report.report_config import ReportConfig

# Test data
valid_config = {
    "jql": "project = FR AND sprint in openSprints()",
    "google_sheet": "jira"
}
valid_config_json = json.dumps(valid_config)


def test_report_config_valid():
    # Create a temporary JSON file with valid configuration
    with open('temp_config.json', 'w') as file:
        file.write(valid_config_json)

    # Test loading valid configuration
    config = ReportConfig.from_json('temp_config.json')
    assert config.jql == valid_config['jql']
    assert config.google_sheet == valid_config['google_sheet']

    # Cleanup
    os.remove('temp_config.json')


def test_report_config_file_not_found():
    with pytest.raises(FileNotFoundError):
        _ = ReportConfig.from_json('non_existent_config.json')


def test_report_config_invalid_json():
    # Create a temporary JSON file with invalid JSON
    with open('temp_invalid_config.json', 'w') as file:
        file.write("{invalid_json}")

    with pytest.raises(ValueError):
        _ = ReportConfig.from_json('temp_invalid_config.json')

    # Cleanup
    os.remove('temp_invalid_config.json')
