from fetch_github import fetch_github_activity

username = "Fr4cas"

activity = fetch_github_activity(username)

# for event in activity:
#     print(event)

# commit_dates = [event["created_at"][:10] for event in activity]
# print("Commit dates:")
# print(commit_dates)

commit_counts = fetch_github_activity(username)

print("Commits per day:")
for date, count in commit_counts.items():
    print(f"{date}: {count}")