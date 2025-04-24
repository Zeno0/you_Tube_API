import requests
import csv
import datetime
import os

# 🔹 Your YouTube API Key
API_KEY = os.environ.get('GOOGLE_API')
# VIDEO_ID = "fPr4jUsByDQ&t" # crunchyroll anime awards
VIDEO_ID = "rACLlmnM-IM"
# CHANNEL_ID = "YOUR_CHANNEL_ID"  # You can extract from video data

# 🔹 Fetch Video Statistics
video_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id={VIDEO_ID}&key={API_KEY}"
video_data = requests.get(video_url).json()

# Extract video details
video_info = video_data["items"][0]
title = video_info["snippet"]["title"]
# description = video_info["snippet"]["description"]
views = video_info["statistics"]["viewCount"]
likes = video_info["statistics"].get("likeCount", "N/A")  # Some videos disable likes
comments = video_info["statistics"].get("commentCount", "N/A")
duration = video_info["contentDetails"]["duration"]
upload_date = video_info["snippet"]["publishedAt"]
channel_id = video_info["snippet"]["channelId"]
video_url = f"https://www.youtube.com/watch?v={VIDEO_ID}"

# 🔹 Fetch Channel Statistics
channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={API_KEY}"
channel_data = requests.get(channel_url).json()

# Extract channel details
channel_info = channel_data["items"][0]
channel_name = channel_info["snippet"]["title"]
subscribers = channel_info["statistics"]["subscriberCount"]
total_videos = channel_info["statistics"]["videoCount"]
total_views = channel_info["statistics"]["viewCount"]
channel_created_date = channel_info["snippet"]["publishedAt"]
channel_url = f"https://www.youtube.com/channel/{channel_id}"

# 🔹 Save to CSV File
csv_file = "youtube_stats.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write headers if the file is new
    if not file_exists:
        writer.writerow([
            "Date", "Video Title", "Views", "Likes", "Comments",
            "Duration", "Upload Date", "Video URL", "Channel Name", "Subscribers",
            "Total Videos", "Total Views", "Channel Created Date", "Channel URL"
        ])

    # Write video and channel data
    writer.writerow([
        datetime.datetime.now(), title, views, likes, comments,
        duration, upload_date, video_url, channel_name, subscribers,
        total_videos, total_views, channel_created_date, channel_url
    ])

print("✅ YouTube statistics saved to CSV!")

# Git commit function
def commit_and_push():
    os.system("git config --global user.email 'github-actions@github.com'")
    os.system("git config --global user.name 'GitHub Actions'")
    os.system("git add youtube_stats.csv")
    os.system('git commit -m "Updated YouTube stats"')
    os.system("git push")

# Run commit after fetching stats
commit_and_push()
