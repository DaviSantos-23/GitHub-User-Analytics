import plotly.express as px
import pandas as pd


class Charts:

    @staticmethod
    def languages_chart(languages):

        if not languages:

            return px.bar(
                title="Nenhuma linguagem encontrada."
            )

        df = pd.DataFrame({

            "Linguagem": list(languages.keys()),

            "Quantidade": list(languages.values())

        })

        fig = px.bar(

            df,

            x="Linguagem",

            y="Quantidade",

            text="Quantidade",

            title="💻 Linguagens Mais Utilizadas"

        )

        fig.update_layout(

            template="plotly_white",

            xaxis_title="",

            yaxis_title="Quantidade"

        )

        return fig


    @staticmethod
    def languages_pie_chart(languages):

        if not languages:

            return px.pie(
                title="Nenhuma linguagem encontrada."
            )

        df = pd.DataFrame({

            "Linguagem": list(languages.keys()),

            "Quantidade": list(languages.values())

        })

        fig = px.pie(

            df,

            names="Linguagem",

            values="Quantidade",

            title="🥧 Distribuição das Linguagens"

        )

        fig.update_layout(

            template="plotly_white"

        )

        return fig


    @staticmethod
    def stars_chart(repositories):

        if not repositories:

            return px.bar(
                title="Nenhum repositório encontrado."
            )

        df = pd.DataFrame({

            "Repositório":[
                repo["name"]
                for repo in repositories
            ],

            "Stars":[
                repo["stargazers_count"]
                for repo in repositories
            ]

        })

        df = df.sort_values(

            by="Stars",

            ascending=False

        ).head(10)

        fig = px.bar(

            df,

            x="Repositório",

            y="Stars",

            text="Stars",

            title="⭐ Top 10 Repositórios por Stars"

        )

        fig.update_layout(

            template="plotly_white",

            xaxis_title="",

            yaxis_title="Stars"

        )

        return fig