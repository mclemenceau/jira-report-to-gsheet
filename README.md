# JIRA Report Generator

This Python script is designed to query JIRA issues and export the details to a Google Sheet.

## Description

The script uses the JIRA Python Library to connect to a JIRA instance and retrieve issue data based on a specified JQL (JIRA Query Language) query. The results are then formatted and exported to a specified Google Sheet, allowing for easy viewing and analysis of the data.

## Configuration
The report can be configured by creating a json configuration file that contains a few fields:
```json
{                                                                                 
    'fields': "List of Jira Properties"
    'google_sheet': "Name of Google Sheet Document",
    'google_sheet_name': "Name of the sheet where to import data",
    'jql': "The Jira request that will return the list of issues"
}
```
### Jira issues properties
At this time this script imports the following information for each Jira issues part of the JQL results:
 - IssueType : Bug, Task, Story, ...
 - Key : The Jira unique ID (FR-123)
 - FixVersions
 - Assignee
 - Epic : The Epic ID
 - Summary
 - Priority
 - Status
 - Created : date isue was created
 - Resolution
 - Resolved : date issue was resolved
 - Components : the list of impacted components
 - Sprint : the last sprints this issue was part of
 - StoryPoints

Each of this field will be imported in the targeted Google Sheet where each Field will be a column and one line per Jira issue

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
