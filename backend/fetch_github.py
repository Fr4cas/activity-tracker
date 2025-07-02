import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events/public"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json() 

    except requests.exceptions.RequestException as e:
        print("Error fetching GitHub data:", e)
        return []