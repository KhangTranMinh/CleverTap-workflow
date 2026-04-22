"""Jira REST API client for CleverTap workflow."""

import os
import json
import base64
from typing import Optional
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


class JiraClient:
    def __init__(self):
        self.base_url = os.environ["JIRA_URL"].rstrip("/")
        email = os.environ["JIRA_EMAIL"]
        token = os.environ["JIRA_API_TOKEN"]
        credentials = base64.b64encode(f"{email}:{token}".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> dict:
        url = f"{self.base_url}/rest/api/3/{path}"
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, headers=self.headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            raise RuntimeError(f"Jira API error {e.code}: {error_body}") from e

    def create_issue(
        self,
        summary: str,
        description: str,
        assignee_id: str,
        story_points: int,
        labels: list[str],
        due_date: Optional[str] = None,
        parent_key: Optional[str] = None,
    ) -> dict:
        project_key = os.environ["JIRA_PROJECT_KEY"]
        fields: dict = {
            "project": {"key": project_key},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}],
                    }
                ],
            },
            "issuetype": {"name": "Story"},
            "assignee": {"accountId": assignee_id},
            "labels": labels,
            "story_points": story_points,
        }
        if due_date:
            fields["duedate"] = due_date
        if parent_key:
            fields["parent"] = {"key": parent_key}

        return self._request("POST", "issue", {"fields": fields})

    def create_epic(self, name: str, summary: str, labels: list[str]) -> dict:
        project_key = os.environ["JIRA_PROJECT_KEY"]
        fields = {
            "project": {"key": project_key},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": name}],
                    }
                ],
            },
            "issuetype": {"name": "Epic"},
            "labels": labels,
        }
        return self._request("POST", "issue", {"fields": fields})

    def get_issue(self, issue_key: str) -> dict:
        return self._request("GET", f"issue/{issue_key}")

    def search_issues(self, jql: str) -> dict:
        return self._request("POST", "issue/bulk", {"jql": jql})
