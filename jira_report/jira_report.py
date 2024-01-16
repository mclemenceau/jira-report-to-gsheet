#!/usr/bin/python3

from argparse import ArgumentParser
import os

import gspread

from jira_report.jira_manager import JiraManager
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

    HEADERS = ['Issue Type',
               'Key',
               'Fix versions',
               'Assignee',
               'Epic Link',
               'Summary',
               'Priority',
               'Status',
               'Created',
               'Resolution',
               'Resolved',
               'Components',
               'Sprint',
               'Story Points']

    DATAROOT = "A2"
    DATAEND = "N"

    issues_details = []
    for issue in jira_issues:
        issues_details.append(
            [issue.fields.issuetype.name,
             issue.key,
             ';'.join(version.name for version in issue.fields.fixVersions),
             issue.fields.assignee.displayName,
             issue.fields.customfield_10014,            # Epic
             issue.fields.summary,
             issue.fields.priority.name,
             issue.fields.status.name,
             issue.fields.created,
             issue.fields.resolution.name if issue.fields.resolution else "",
             issue.fields.resolutiondate,
             ';'.join(component.name for component in issue.fields.components),
             (issue.fields.customfield_10020[-1].name
              if issue.fields.customfield_10020 else ""),
             issue.fields.customfield_10024,            # Story Points
             ])

    gc = gspread.oauth()
    sh = gc.open(config.google_sheet)

    SHEET = sh.worksheet(config.google_sheet_name)
    SHEET.clear()
    SHEET.update("A1:N1", [HEADERS])

    RANGE = f"{DATAROOT}:{DATAEND}{len(issues_details)+1}"

    SHEET.update(RANGE, issues_details)

    return 0
