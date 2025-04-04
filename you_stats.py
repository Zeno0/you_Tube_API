import requests
import csv
from datetime import datetime
import os

# 🔹 Replace with your actual API key
API_KEY = "AIzaSyCkHqOelqQVvtYRQx8vUAuE-HP5fFqHGD0"

# 🔹 Replace with the YouTube Video ID you want to track
# updated video id of anime awards fPr4jUsByDQ&t
VIDEO_ID = "fPr4jUsByDQ&t"  
# Construct the API request URL
url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}"

# Send GET request
response = requests.get(url)
data = response.json()

# Extract statistics
if "items" in data and data["items"]:
    stats = data["items"][0]["statistics"]
    views = stats.get("viewCount", "N/A")
    likes = stats.get("likeCount", "N/A")
    comments = stats.get("commentCount", "N/A")
    
    print(f"Views: {views}")
    print(f"Likes: {likes}")
    print(f"Comments: {comments}")

    # 🔹 Save to CSV File
    filename = "youtube_stats.csv"
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), VIDEO_ID, views, likes, comments])

    print(f"✅ Data saved to {filename}")

else:
    print("❌ Invalid Video ID or API Limit Exceeded")


# Git commit function
def commit_and_push():
    os.system("git config --global user.email 'github-actions@github.com'")
    os.system("git config --global user.name 'GitHub Actions'")
    os.system("git add youtube_stats.csv")
    os.system('git commit -m "Updated YouTube stats"')
    os.system("git push")

# Run commit after fetching stats
commit_and_push()
