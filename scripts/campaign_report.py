"""Pull and format CleverTap campaign performance reports."""

import argparse
import json
import os
import urllib.request
from typing import Optional
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

BENCHMARKS = {
    "push": {"delivered_rate": 0.85, "open_rate": 0.20, "ctr": 0.04, "conversion": 0.02},
    "email": {"delivered_rate": 0.95, "open_rate": 0.25, "ctr": 0.03, "conversion": 0.01},
    "sms": {"delivered_rate": 0.95, "open_rate": 0.90, "ctr": 0.06, "conversion": 0.03},
    "in_app": {"delivered_rate": 1.0, "open_rate": 0.85, "ctr": 0.12, "conversion": 0.07},
}


def fetch_stats(campaign_id: str) -> dict:
    account_id = os.environ["CLEVERTAP_ACCOUNT_ID"]
    passcode = os.environ["CLEVERTAP_PASSCODE"]
    url = f"https://api.clevertap.com/1/targets/{campaign_id}/result.json"
    headers = {
        "X-CleverTap-Account-Id": account_id,
        "X-CleverTap-Passcode": passcode,
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def fetch_campaigns(from_date: str, to_date: str) -> list[dict]:
    account_id = os.environ["CLEVERTAP_ACCOUNT_ID"]
    passcode = os.environ["CLEVERTAP_PASSCODE"]
    url = f"https://api.clevertap.com/1/targets/list.json?from={from_date}&to={to_date}"
    headers = {
        "X-CleverTap-Account-Id": account_id,
        "X-CleverTap-Passcode": passcode,
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    return data.get("targets", [])


def rate(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "N/A"
    return f"{(numerator / denominator * 100):.1f}%"


def flag(value: float, benchmark: float) -> str:
    return "OK" if value >= benchmark else "LOW"


def print_report(stats: dict, channel: str = "push") -> None:
    bench = BENCHMARKS.get(channel, BENCHMARKS["push"])

    sent = stats.get("sent", 0)
    delivered = stats.get("delivered", 0)
    opens = stats.get("opens", 0)
    clicks = stats.get("clicks", 0)
    converted = stats.get("converted", 0)

    delivered_rate = delivered / sent if sent else 0
    open_rate = opens / delivered if delivered else 0
    ctr = clicks / delivered if delivered else 0
    conv_rate = converted / delivered if delivered else 0

    print(f"\n{'='*60}")
    print(f"Campaign: {stats.get('name', stats.get('id', 'Unknown'))}")
    print(f"Channel:  {channel.upper()}")
    print(f"{'='*60}")
    print(f"{'Metric':<20} {'Count':>8} {'Rate':>8} {'Status':>8}")
    print(f"{'-'*20} {'-'*8} {'-'*8} {'-'*8}")
    print(f"{'Sent':<20} {sent:>8,}")
    print(f"{'Delivered':<20} {delivered:>8,} {rate(delivered, sent):>8} {flag(delivered_rate, bench['delivered_rate']):>8}")
    print(f"{'Opened':<20} {opens:>8,} {rate(opens, delivered):>8} {flag(open_rate, bench['open_rate']):>8}")
    print(f"{'Clicked':<20} {clicks:>8,} {rate(clicks, delivered):>8} {flag(ctr, bench['ctr']):>8}")
    print(f"{'Converted':<20} {converted:>8,} {rate(converted, delivered):>8} {flag(conv_rate, bench['conversion']):>8}")

    print(f"\nBenchmarks ({channel}):")
    print(f"  Delivery: {bench['delivered_rate']*100:.0f}% | Open: {bench['open_rate']*100:.0f}% | CTR: {bench['ctr']*100:.0f}% | Conv: {bench['conversion']*100:.0f}%")

    # Recommendations
    issues = []
    if delivered_rate < bench["delivered_rate"]:
        issues.append("Low delivery rate — check push token validity or email bounces")
    if open_rate < bench["open_rate"]:
        issues.append("Low open rate — consider sending time, sender name, or subject line A/B test")
    if ctr < bench["ctr"]:
        issues.append("Low CTR — test different copy, CTA button text, or offer")
    if conv_rate < bench["conversion"]:
        issues.append("Low conversion — check deep link destination, offer relevance, landing experience")

    if issues:
        print("\nRecommendations:")
        for i in issues:
            print(f"  ! {i}")
    else:
        print("\nAll metrics above benchmark.")


def main():
    parser = argparse.ArgumentParser(description="CleverTap campaign performance report")
    parser.add_argument("--campaign-id", help="Single campaign ID")
    parser.add_argument("--from-date", help="Date range start YYYYMMDD")
    parser.add_argument("--to-date", help="Date range end YYYYMMDD")
    parser.add_argument("--channel", default="push", choices=["push", "email", "sms", "in_app"])
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if args.campaign_id:
        stats = fetch_stats(args.campaign_id)
        if args.json:
            print(json.dumps(stats, indent=2))
        else:
            print_report(stats, channel=args.channel)
    elif args.from_date and args.to_date:
        campaigns = fetch_campaigns(args.from_date, args.to_date)
        print(f"\nFound {len(campaigns)} campaigns between {args.from_date} and {args.to_date}")
        for c in campaigns:
            try:
                stats = fetch_stats(c["id"])
                if args.json:
                    print(json.dumps({**c, **stats}, indent=2))
                else:
                    stats["name"] = c.get("name", c["id"])
                    print_report(stats, channel=args.channel)
            except Exception as e:
                print(f"  Error fetching {c['id']}: {e}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
