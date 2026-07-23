import requests


class GitHubAPI:

    BASE_URL = "https://api.github.com"


    @staticmethod
    def get_user(username):

        url = f"{GitHubAPI.BASE_URL}/users/{username}"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        return response.json()


    @staticmethod
    def get_repositories(username):

        url = f"{GitHubAPI.BASE_URL}/users/{username}/repos"

        response = requests.get(url)

        if response.status_code != 200:
            return []

        repos = response.json()

        repos.sort(
            key=lambda repo: repo["stargazers_count"],
            reverse=True
        )

        return repos