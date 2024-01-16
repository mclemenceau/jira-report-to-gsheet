#!/usr/bin/python3

from argparse import ArgumentParser
import os

import gspread

from jira_report.jira_manager import JiraManager
from jira_report.jira_issue import JiraIssue
from jira_report.report_config import ReportConfig


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument(
        '-c', '--config',
        default='config.json',
        help='Path to the configuration file. Default is "config.json".',
        nargs='?',
        const='config.json')

    args = parser.parse_args()

    if not os.path.isfile(args.config):
        parser.error(f"The file {args.config} file does not exist.")
        return 1

    config = ReportConfig.from_json(args.config)

    try:
        jira = JiraManager()
    except ValueError as e:
        raise ValueError("ERROR: Cannot initialize Jira API") from e

    jira_issues = jira.query(config.jql)

    DATAROOT = "A2"
    # TODO find the range according the list of fields
    DATAEND = "N"

    issues_details = []
    for issue in jira_issues:
        issues_details.append(JiraIssue(issue).fields(config.fields))

    gc = gspread.oauth()
    sh = gc.open(config.google_sheet)

    SHEET = sh.worksheet(config.google_sheet_name)
    SHEET.clear()
    SHEET.update("A1:N1", [config.fields])

    RANGE = f"{DATAROOT}:{DATAEND}{len(issues_details)+1}"

    SHEET.update(RANGE, issues_details)

    return 0
