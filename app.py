from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    try:
        df = pd.read_csv("youtube_stats.csv")
        latest = df.iloc[-1]
        return render_template("index.html", data=latest)
    except Exception as e:
        return f"<h2>Error loading data: {e}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
