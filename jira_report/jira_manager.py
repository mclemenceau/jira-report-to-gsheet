from typing import List
from jira import JIRA
from jira_report.jira_config import jira_config


class JiraManager:
    """
    JiraManager class is used to simplify access to Jira data.
    It automates the connection to the Jira API using the jira_config class

    Methods:
        query: query Jira for a JQL and return a list of Jira Objects

    """
    def __init__(self):
        jira_cfg = jira_config()
        self.jira = JIRA(
            jira_cfg.server,
            basic_auth=(jira_cfg.login, jira_cfg.token))

    def query(self, jql) -> List:
        """
        Query JIRA for issues based on the provided JQL query.

        Args:
            jql (str): The JQL query string.

        Returns:
            list: List of JIRA issues.
        """
        issue_index = 0
        issue_batch = 50

        jira_objects = []

        while True:
            start_index = issue_index * issue_batch
            # jql = "project = FR AND labels = RoadmapItem"
            issues = self.jira.search_issues(jql, startAt=start_index)
            if not issues:
                break
            issue_index += 1

            for issue in issues:
                jira_objects.append(issue)

        return jira_objects
