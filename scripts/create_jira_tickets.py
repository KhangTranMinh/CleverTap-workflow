"""Create Jira tickets from a campaign plan Markdown file."""

import argparse
import os
import re
import sys
from typing import Optional
from dotenv import load_dotenv
from jira_client import JiraClient

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

ASSIGNEE_MAP = {
    "minh": os.environ.get("JIRA_USER_MINH", ""),
    "linh": os.environ.get("JIRA_USER_LINH", ""),
    "duc": os.environ.get("JIRA_USER_DUC", ""),
}


def parse_plan(plan_path: str) -> dict:
    """Parse a plan Markdown file into structured data."""
    with open(plan_path) as f:
        content = f.read()

    plan: dict = {"title": "", "tasks": []}

    # Extract title (first H1)
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        plan["title"] = title_match.group(1).strip()

    # Extract tasks section
    tasks_section = re.search(
        r"## Tasks\n(.*?)(?=\n## |\Z)", content, re.DOTALL
    )
    if not tasks_section:
        print("Warning: No '## Tasks' section found in plan")
        return plan

    tasks_text = tasks_section.group(1)

    # Parse task rows from markdown table
    # Expected format: | Task Title | Description | Assignee | Points | Due Date |
    table_rows = re.findall(
        r"^\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]*)\s*\|",
        tasks_text,
        re.MULTILINE,
    )

    for row in table_rows:
        title, description, assignee, points_str, due = [
            c.strip() for c in row
        ]
        # Skip header row
        if title.lower() in ("task", "title", "---"):
            continue
        try:
            points = int(re.search(r"\d+", points_str).group())
        except (AttributeError, ValueError):
            points = 1

        plan["tasks"].append(
            {
                "title": title,
                "description": description,
                "assignee": assignee.lower(),
                "points": points,
                "due": due if due else None,
            }
        )

    return plan


def create_tickets(plan_path: str, dry_run: bool = False) -> None:
    plan = parse_plan(plan_path)

    if not plan["tasks"]:
        print("No tasks found in plan. Check that your plan has a ## Tasks section with a table.")
        sys.exit(1)

    client = JiraClient() if not dry_run else None

    print(f"\nPlan: {plan['title']}")
    print(f"Tasks found: {len(plan['tasks'])}\n")

    # Create epic
    epic_key: Optional[str] = None
    if not dry_run and client:
        print(f"Creating Epic: {plan['title']} ...")
        epic = client.create_epic(
            name=plan["title"],
            summary=f"[CRM] {plan['title']}",
            labels=["clevertap", "crm"],
        )
        epic_key = epic.get("key")
        print(f"  Epic created: {epic_key}")

    print("\nCreating story tickets:")
    print("-" * 60)

    results = []
    for task in plan["tasks"]:
        assignee_name = task["assignee"]
        assignee_id = ASSIGNEE_MAP.get(assignee_name, "")

        if not assignee_id and not dry_run:
            print(f"  WARNING: No Jira ID configured for '{assignee_name}'. Check .env.")

        labels = ["clevertap", "crm"]
        title_lower = task["title"].lower()
        if "campaign" in title_lower or "push" in title_lower or "segment" in title_lower:
            labels.append("campaign")
        elif "track" in title_lower or "event" in title_lower or "qa" in title_lower:
            labels.append("tracking")

        if dry_run:
            key = f"DRY-{len(results)+1}"
            print(f"  [DRY RUN] {key}: {task['title']}")
            print(f"    → Assignee: {assignee_name} | Points: {task['points']} | Due: {task['due'] or 'TBD'}")
        else:
            ticket = client.create_issue(
                summary=f"[CRM] {task['title']}",
                description=task["description"],
                assignee_id=assignee_id,
                story_points=task["points"],
                labels=labels,
                due_date=task["due"],
                parent_key=epic_key,
            )
            key = ticket.get("key", "?")
            print(f"  {key}: {task['title']}")
            print(f"    → {assignee_name} | {task['points']}pts | due: {task['due'] or 'TBD'}")

        results.append({"key": key, **task})

    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Epic: {epic_key or 'N/A'}")
    print(f"  Tickets created: {len(results)}")
    for r in results:
        print(f"  {r['key']:12} {r['assignee']:6} {r['title']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Jira tickets from a plan MD file")
    parser.add_argument("--plan", required=True, help="Path to plan markdown file")
    parser.add_argument("--dry-run", action="store_true", help="Preview tickets without creating")
    args = parser.parse_args()
    create_tickets(args.plan, dry_run=args.dry_run)
