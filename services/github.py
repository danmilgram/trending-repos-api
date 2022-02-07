import os
import requests

github_api_url = os.environ.get("GITHUB_API_URL")
github_search_url = os.environ.get("GITHUB_SEARCH_REPO_URL")

class GitHubService():

    @classmethod
    def _fetch_trending_repos(cls,date):
        url = "{gh}{s}?q=created:>{d}&sort=stars&order=desc&per_page=100".format(
            gh = github_api_url,
            s = github_search_url,
            d = date 
        )

        return requests.get(url).json()

    @classmethod
    def get_trending_repos(cls, date):
        response = cls._fetch_trending_repos(date)

        items = {}
        for r in response["items"]:

            lang = r["language"]
            url = r["html_url"]
            desc = r["description"]

            if not lang:
                lang = "undefined"

            if items.get(lang) is None:
                items[lang] = {
                    "count": 0 ,
                    "repos":[]
                }

            items[lang]["repos"].append({
                "url": url,
                "description": desc
            })
            items[lang]["count"] += 1

        return items






        