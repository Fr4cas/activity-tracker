from fetch_github import fetch_github_activity

username = "Fr4cas"

activity = fetch_github_activity(username)

for event in activity:
    print(event)