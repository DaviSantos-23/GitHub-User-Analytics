from src.analytics import Analytics


class Statistics:

    @staticmethod
    def generate(repositories):

        languages = Analytics.languages(repositories)

        return {

            "total_stars": Analytics.total_stars(repositories),

            "total_forks": Analytics.total_forks(repositories),

            "languages": languages,

            "top_repositories": Analytics.top_repositories(
                repositories
            ),

            "best_repository": Analytics.best_repository(
                repositories
            ),

            "main_language": Analytics.main_language(
                languages
            ),

            "average_stars": Analytics.average_stars(
                repositories
            )

        }