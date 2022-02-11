import os
import requests

github_api_url = os.environ.get("GITHUB_API_URL")
github_search_url = os.environ.get("GITHUB_SEARCH_REPO_URL")


class GitHubService:
    @classmethod
    def _fetch_trending_repos(cls, date):
        url = "{gh}{s}?q=created:>{d}&sort=stars&order=desc&per_page=100".format(
            gh=github_api_url, s=github_search_url, d=date
        )

        return requests.get(url).json()

    @classmethod
    def get_trending_repos(cls, date):
        response = cls._fetch_trending_repos(date)

        items = []
        for r in response["items"]:
            id = r["id"]
            lang = r["language"]
            url = r["html_url"]
            desc = r["description"]

            if not lang:
                lang = "undefined"

            found_lang = False
            for x in items:
                if x.get("language") == lang:
                    x["repos"].append({
                        "url": url, 
                        "description": desc,
                        "id":id
                    })
                    x["count"] += 1
                    found_lang = True

            if not found_lang:
                items.append(
                    {
                        "language": lang,
                        "count": 1,
                        "repos": [{
                            "url": url, 
                            "description": desc,
                            "id":id
                        }],
                    }
                )

        return {"data": items}
