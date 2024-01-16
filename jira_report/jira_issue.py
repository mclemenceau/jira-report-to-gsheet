from typing import List


class JiraIssue:

    def __init__(self, issue):
        self.issue = issue
        self.field_mappings = {
            "IssueType": lambda: self.issue.fields.issuetype.name,
            "Key": lambda: self.issue.key,
            "FixVersions": lambda:
                (';'.join(
                    version.name for version in self.issue.fields.fixVersions
                    )),
            "Assignee": lambda:
                (self.issue.fields.assignee.displayName
                 if self.issue.fields.assignee else ""),
            "Epic": lambda: self.issue.fields.customfield_10014,
            "Summary": lambda: self.issue.fields.summary,
            "Priority": lambda: self.issue.fields.priority.name,
            "Status": lambda: self.issue.fields.status.name,
            "Created": lambda: self.issue.fields.created,
            "Resolution": lambda:
                (self.issue.fields.resolution.name
                 if self.issue.fields.resolution else ""),
            "ResolutionDate": lambda: self.issue.fields.resolutiondate,
            "Components": lambda:
                (';'.join(component.name
                          for component in self.issue.fields.components)),
            "Sprint": lambda:
                (self.issue.fields.customfield_10020[-1].name
                 if self.issue.fields.customfield_10020 else ""),
            "StoryPoints": lambda: self.issue.fields.customfield_10024,
            # Add more fields here as needed
        }

    def field(self, field_name: str) -> str:
        get_field = self.field_mappings.get(field_name)
        return get_field() if get_field else None

    def fields(self, fields_list: List) -> List:
        return [self.field(x) for x in fields_list]
