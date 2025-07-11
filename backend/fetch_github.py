import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Get event data from user profile
def fetch_github_activity(username):
    token = os.getenv("GITHUB_TOKEN")
    base_url = f"https://api.github.com/users/{username}/events/public"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}" if token else None
        }
    
    all_events = []
    
    for page in range(1,11):
        url = f"{base_url}?page={page}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        page_events = response.json()
        
        if not page_events:
            break
        
        all_events.extend(page_events)
    
    contrib_events = all_events
    dates_seen = [event["created_at"][:10] for event in all_events]
    print(sorted(set(dates_seen)))
    
    for event in all_events:
        created = event.get("created_at", "")
        if "2025-06-25" in created or "2025-06-26" in created or "2025-06-27" in created:
            print("=" * 60)
            print(f"{event['type']} - {created}")
            if event["type"] == "PushEvent":
                for commit in event["payload"].get("commits", []):
                    print(f"Commit by {commit['author']['name']}: {commit['message']}")
    
    # push_events = [event for event in all_events if event["type"] == "PushEvent"]
    
    contrib_dates = [event["created_at"][:10] for event in contrib_events]
        
    contrib_counts = {}
    for date in contrib_dates:
        if date in contrib_counts:
            contrib_counts[date] += 1
        else:
            contrib_counts[date] = 1

    return contrib_counts
    
if __name__ == "__main__":
    username = "Fr4cas"
    data = fetch_github_activity(username)
    
    with open("../frontend/public/data.json", "w") as f:
        json.dump(data, f, indent=2)
        
    print("data saved to frontend")