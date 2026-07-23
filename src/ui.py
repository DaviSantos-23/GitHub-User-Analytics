import streamlit as st
import pandas as pd

from src.formatter import Formatter
from src.charts import Charts
from src.exporter import CSVExporter


class UI:

    @staticmethod
    def configure_page():

        st.set_page_config(
            page_title="GitHub User Analytics",
            page_icon="🐙",
            layout="wide"
        )

    @staticmethod
    def sidebar():

        with st.sidebar:

            st.title("🐙 GitHub Analytics")

            st.caption(
                "Dashboard desenvolvido em Python utilizando a API pública do GitHub."
            )

            st.divider()

            st.subheader("Tecnologias")

            tecnologias = [
                "Python",
                "Streamlit",
                "Requests",
                "Pandas",
                "Plotly",
                "GitHub REST API"
            ]

            for tecnologia in tecnologias:

                st.success(tecnologia)

            st.divider()

            st.info(
                "Digite um usuário e clique em Buscar."
            )


    @staticmethod
    def header():

        st.title("🐙 GitHub User Analytics")

        st.caption(
            "Analise qualquer perfil público do GitHub."
        )


    @staticmethod
    def search_box():

        return st.text_input(

            "Digite um usuário",

            placeholder="Ex.: torvalds"

        ).strip()


    @staticmethod
    def search_button():

        return st.button(

            "🔍 Buscar",

            use_container_width=True

        )
    @staticmethod
    def show_profile(data, account_age):

        col1, col2 = st.columns([1, 3])

        with col1:

            if data["avatar"]:

                st.image(
                    data["avatar"],
                    width=180
                )
            

        with col2:

            st.subheader(data["name"])

            st.caption(f"@{data['login']}")

            st.write(data["bio"])

            st.write(f"🏢 **Empresa:** {data['company']}")

            st.write(f"📍 **Localização:** {data['location']}")

            st.write(f"📅 Criado em: {Formatter.format_date(data['created_at'])}")

            st.write(f"⏳ **Tempo no GitHub:** {account_age}")

            st.link_button(
                "🔗 Abrir Perfil",
                data["profile"]
            )

        st.divider()


    @staticmethod
    def show_metrics(data, stats):

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "👥 Seguidores",
            Formatter.format_number(
                data["followers"]
            )
        )

        c2.metric(
            "📦 Repositórios",
            Formatter.format_number(
                data["repositories"]
            )
        )

        c3.metric(
            "⭐ Stars",
            Formatter.format_number(
                stats["total_stars"]
            )
        )

        c4.metric(
            "🍴 Forks",
            Formatter.format_number(
                stats["total_forks"]
            )
        )

        st.divider()


    @staticmethod
    def show_best_repository(stats):

        repo = stats["best_repository"]

        st.subheader("🏆 Repositório Destaque")

        if repo is None:

            st.info(
                "Nenhum repositório encontrado."
            )

            return

        st.success(

            f"""
    ### {repo['name']}

    ⭐ Stars: {Formatter.format_number(repo['stargazers_count'])}

    🍴 Forks: {Formatter.format_number(repo['forks_count'])}

    💻 Linguagem: {repo['language'] or '-'}
    """
        )

        st.divider()

    @staticmethod
    def show_graphs(stats, repos):

        col1, col2 = st.columns(2)

        with col1:

            fig = Charts.languages_chart(
                stats["languages"]
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                key="languages_chart"
            )

        with col2:

            pie = Charts.languages_pie_chart(
                stats["languages"]
            )

            st.plotly_chart(
                pie,
                use_container_width=True,
                key="languages_pie"
            )

        st.divider()

        fig = Charts.stars_chart(repos)

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="stars_chart"
        )

        st.divider()

    @staticmethod
    def show_table(stats):

        st.subheader("🏆 Top 5 Repositórios")

        repos = stats["top_repositories"]

        if not repos:

            st.info("Nenhum repositório encontrado.")

            return

        df = pd.DataFrame({

            "Repositório":[
                r["name"]
                for r in repos
            ],

            "⭐ Stars":[
                r["stargazers_count"]
                for r in repos
            ],

            "🍴 Forks":[
                r["forks_count"]
                for r in repos
            ],

            "👀 Watchers":[
                r["watchers_count"]
                for r in repos
            ],

            "💻 Linguagem":[
                r["language"] or "-"
                for r in repos
            ]

        })

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

    @staticmethod
    def show_export(username, repos):

        st.subheader("📥 Exportar Dados")

        csv = CSVExporter.export(repos)

        if not repos:

            st.info("Não há dados para exportar.")

            return

        st.download_button(

            "⬇️ Baixar CSV",

            csv,

            file_name=f"{username}_github.csv",

            mime="text/csv"

        )

        st.divider()

    @staticmethod
    def show_statistics(stats):

        st.subheader("📈 Estatísticas")

        c1, c2 = st.columns(2)

        with c1:

            st.success(

                f"""
    ⭐ Total de Stars

    {Formatter.format_number(stats["total_stars"])}
    """
            )

            st.success(

                f"""
    🍴 Total de Forks

    {Formatter.format_number(stats["total_forks"])}
    """
            )

        with c2:

            st.success(

                f"""
    💻 Linguagem Principal

    {stats["main_language"]}
    """
            )

            st.success(

                f"""
    ⭐ Média de Stars

    {stats["average_stars"]}
    """
            )

        st.divider()

    @staticmethod
    def show_history():

        with st.sidebar:

            st.divider()

            st.subheader("🕒 Histórico")

            if "history" not in st.session_state:

                st.session_state.history = []

            if st.session_state.history:

                for user in reversed(st.session_state.history):

                    st.write(f"• {user}")

            else:

                st.caption(
                    "Nenhuma pesquisa realizada."
                )

            if st.button("🗑 Limpar Histórico"):

                st.session_state.history = []

                st.rerun()
    @staticmethod
    def footer():

        st.divider()

        st.caption(

            "Desenvolvido com ❤️ utilizando Python, Streamlit, Plotly e GitHub REST API."

        )