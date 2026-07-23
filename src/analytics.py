from collections import Counter
from datetime import datetime


class Analytics:

    @staticmethod
    def total_stars(repositories):

        return sum(
            repo["stargazers_count"]
            for repo in repositories
        )

    @staticmethod
    def total_forks(repositories):

        return sum(
            repo["forks_count"]
            for repo in repositories
        )

    @staticmethod
    def languages(repositories):

        languages = Counter()

        for repo in repositories:

            language = repo.get("language")

            if language:

                languages[language] += 1

        return dict(languages)

    @staticmethod
    def top_repositories(repositories, limit=5):

        return sorted(

            repositories,

            key=lambda repo: repo["stargazers_count"],

            reverse=True

        )[:limit]

    @staticmethod
    def best_repository(repositories):

        if not repositories:

            return None

        return max(

            repositories,

            key=lambda repo: repo["stargazers_count"]

        )

    @staticmethod
    def main_language(languages):

        if not languages:

            return "-"

        return max(

            languages,

            key=languages.get

        )

    @staticmethod
    def average_stars(repositories):

        if not repositories:

            return 0

        total = Analytics.total_stars(repositories)

        return round(

            total / len(repositories),

            1

        )

    @staticmethod
    def account_age(created_at):

        created = datetime.strptime(
            created_at,
            "%Y-%m-%dT%H:%M:%SZ"
        )

        today = datetime.today()

        years = today.year - created.year

        if (today.month, today.day) < (created.month, created.day):
            years -= 1

        return f"{years} anos"