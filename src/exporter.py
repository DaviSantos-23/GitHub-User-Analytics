import pandas as pd


class CSVExporter:

    @staticmethod
    def export(repositories):
        """
        Exporta os repositórios para um arquivo CSV.
        """

        if not repositories:
            return ""

        df = pd.DataFrame([
            {
                "Repositório": repo["name"],
                "Descrição": repo["description"] or "-",
                "Linguagem": repo["language"] or "-",
                "Stars": repo["stargazers_count"],
                "Forks": repo["forks_count"],
                "Watchers": repo["watchers_count"],
                "Issues Abertas": repo["open_issues_count"],
                "Criado em": repo["created_at"][:10],
                "Última Atualização": repo["updated_at"][:10],
                "URL": repo["html_url"]
            }
            for repo in repositories
        ])

        return df.to_csv(
            index=False
        ).encode("utf-8")