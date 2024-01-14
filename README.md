# JIRA Report Generator

This Python script is designed to query JIRA issues and export the details to a Google Sheet.

## Description

The script uses the JIRA Python Library to connect to a JIRA instance and retrieve issue data based on a specified JQL (JIRA Query Language) query. The results are then formatted and exported to a specified Google Sheet, allowing for easy viewing and analysis of the data.

## Getting Started

### Dependencies

- Python 3.x
- JIRA Python Library
- gspread (for Google Sheets integration)
- OAuth credentials for Google Sheets API

### Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/mclemenceau/jira-report-to-gsheet
   ```

2. Navigate to the project directory:
    ```bash
    cd jira-report-to-gsheet
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a config.json file with your JIRA and Google Sheets configuration.
    - See example in example in the config directory
  
2. Obtain OAuth credentials from Google Developers Console for Google Sheets API and save them in the project directory.
    - To enable Google API, Google Drive API and Google Sheet API
    - https://docs.gspread.org/en/latest/oauth2.html#for-end-users-using-oauth-client-id

### Usage

Run the script with the following command:
  ```bash
  jira-report-to-gsheet -c path_to_config.json
  ```
Running the script without argument would look for config.json in the current folder
