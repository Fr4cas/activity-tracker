import requests

# Get event data from user profile
def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        events = response.json()
    
        push_events = [event for event in events if event["type"] == "PushEvent"]
        commit_dates = [event["created_at"][:10] for event in push_events]
        
        commit_counts = {}
        for date in commit_dates:
            if date in commit_counts:
                commit_counts[date] += 1
            else:
                commit_counts[date] = 1

        return commit_counts

    except requests.exceptions.RequestException as e:
        print("Error fetching GitHub data:", e)
        return []