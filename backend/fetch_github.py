import requests

# Get event data from user profile
def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
        push_events = [event for event in events if event["type"] == "PushEvent"]
        return push_events

    except requests.exceptions.RequestException as e:
        print("Error fetching GitHub data:", e)
        return []