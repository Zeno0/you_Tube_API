# 📊 YouTube Stats Tracker (Automated via GitHub Actions)

This project uses the YouTube Data API and GitHub Actions to automatically fetch and log video statistics daily. The stats are stored in a CSV file (`youtube_stats.csv`) inside this repository.

---

## 🚀 Features

-  Fetches stats like **views**, **likes**, **comments**, and **more**
-  Runs **daily** using GitHub Actions
-  Appends the latest data to `youtube_stats.csv`

---

## 🔧 How It Works

1. The script `youtube_stats.py` fetches data using the YouTube API.
2. A GitHub Action runs this script automatically each day.
3. The output is saved to `youtube_stats.csv` and committed to the repo.

---

## 📁 Files

| File | Description |
|------|-------------|
| `youtube_stats.py` | Python script that fetches YouTube stats |
| `youtube_stats.csv` | The log file storing daily stats |
| `.github/workflows/...` | GitHub Actions workflow file |

---

## 💡 To-Do / Future Ideas

- [ ] Host a Flask web app to display stats
- [ ] Send daily reports via email or Telegram
- [ ] Visualize trends using matplotlib or Plotly
- [ ] Support multiple YouTube videos/channels

---

## 🙌 Acknowledgements

- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [GitHub Actions](https://docs.github.com/en/actions)
