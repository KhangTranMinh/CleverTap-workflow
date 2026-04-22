"""Set up CleverTap campaigns from a plan Markdown file via REST API."""

import argparse
import os
import re
import json
import sys
import urllib.request
import urllib.error
from typing import Optional
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


class CleverTapClient:
    def __init__(self):
        self.account_id = os.environ["CLEVERTAP_ACCOUNT_ID"]
        self.passcode = os.environ["CLEVERTAP_PASSCODE"]
        self.base_url = "https://api.clevertap.com/1"

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> dict:
        url = f"{self.base_url}/{path}"
        data = json.dumps(body).encode() if body else None
        headers = {
            "X-CleverTap-Account-Id": self.account_id,
            "X-CleverTap-Passcode": self.passcode,
            "Content-Type": "application/json",
        }
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            raise RuntimeError(f"CleverTap API {e.code}: {body}") from e

    def create_segment(self, name: str, description: str, user_ids: list[str]) -> dict:
        payload = {
            "name": name,
            "description": description,
            "source": "manual",
            "users": [{"identity": uid} for uid in user_ids],
        }
        return self._request("POST", "lists/create.json", payload)

    def create_push_campaign(
        self,
        name: str,
        title: str,
        body: str,
        schedule_time: str,
        deep_link: Optional[str] = None,
        segment_name: Optional[str] = None,
    ) -> dict:
        payload: dict = {
            "name": name,
            "when": schedule_time,
            "channel": "push",
            "content": {
                "title": title,
                "body": body,
            },
            "respect_frequency_caps": True,
            "respect_DND": True,
        }
        if deep_link:
            payload["content"]["platform_specific"] = {
                "android": {"deep_link": deep_link},
                "ios": {"deep_link": deep_link},
            }
        if segment_name:
            payload["where"] = {"segment": {"name": segment_name}}
        return self._request("POST", "targets/create.json", payload)

    def get_campaign_stats(self, campaign_id: str) -> dict:
        return self._request("GET", f"targets/{campaign_id}/result.json")

    def list_campaigns(self, from_date: str, to_date: str) -> dict:
        url = f"{self.base_url}/targets/list.json?from={from_date}&to={to_date}"
        headers = {
            "X-CleverTap-Account-Id": self.account_id,
            "X-CleverTap-Passcode": self.passcode,
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())


def parse_campaign_from_plan(plan_path: str) -> dict:
    """Extract campaign details from a plan Markdown file."""
    with open(plan_path) as f:
        content = f.read()

    campaign: dict = {}

    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        campaign["name"] = title_match.group(1).strip()

    # Extract Campaign Details section
    details = re.search(r"## Campaign Details\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if details:
        text = details.group(1)
        for field, key in [
            (r"\*\*Title\*\*[:\s]+(.+)", "title"),
            (r"\*\*Body\*\*[:\s]+(.+)", "body"),
            (r"\*\*Deep Link\*\*[:\s]+(.+)", "deep_link"),
            (r"\*\*Schedule\*\*[:\s]+(.+)", "schedule"),
            (r"\*\*Segment\*\*[:\s]+(.+)", "segment"),
            (r"\*\*Channel\*\*[:\s]+(.+)", "channel"),
        ]:
            m = re.search(field, text)
            if m:
                campaign[key] = m.group(1).strip()

    return campaign


def main():
    parser = argparse.ArgumentParser(description="Set up CleverTap campaigns from a plan")
    parser.add_argument("--plan", help="Path to plan markdown file")
    parser.add_argument(
        "--action",
        choices=["create-segment", "create-campaign", "all", "verify", "list"],
        required=True,
    )
    parser.add_argument("--campaign-id", help="Campaign ID (for verify action)")
    parser.add_argument("--from-date", help="From date YYYYMMDD (for list action)")
    parser.add_argument("--to-date", help="To date YYYYMMDD (for list action)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without executing")
    args = parser.parse_args()

    client = CleverTapClient()

    if args.action == "list":
        from_date = args.from_date or "20240101"
        to_date = args.to_date or "20991231"
        result = client.list_campaigns(from_date, to_date)
        print(json.dumps(result, indent=2))
        return

    if args.action == "verify":
        if not args.campaign_id:
            print("Error: --campaign-id required for verify action")
            sys.exit(1)
        result = client.get_campaign_stats(args.campaign_id)
        print(json.dumps(result, indent=2))
        return

    if not args.plan:
        print("Error: --plan required for this action")
        sys.exit(1)

    campaign = parse_campaign_from_plan(args.plan)
    print(f"Plan loaded: {campaign.get('name', 'Untitled')}")

    if args.action in ("create-campaign", "all"):
        if not campaign.get("title") or not campaign.get("body"):
            print("Error: Plan must have Campaign Details with Title and Body")
            sys.exit(1)

        if args.dry_run:
            print("\n[DRY RUN] Would create campaign:")
            print(json.dumps(campaign, indent=2))
        else:
            result = client.create_push_campaign(
                name=campaign["name"],
                title=campaign["title"],
                body=campaign["body"],
                schedule_time=campaign.get("schedule", ""),
                deep_link=campaign.get("deep_link"),
                segment_name=campaign.get("segment"),
            )
            print("\nCampaign created:")
            print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
