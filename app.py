from datetime import datetime, timedelta
from flask import Flask
from flask import request

from services.github import GitHubService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/trending-repos")
def get_trending_repos():

    date = request.args.get("date", datetime.now().date() - timedelta(days=30))

    return GitHubService.get_trending_repos(date)
