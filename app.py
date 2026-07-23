from src.ui import UI
from src.github_api import GitHubAPI
from src.formatter import Formatter
from src.analytics import Analytics
from src.statistics import Statistics

import streamlit as st


# ==========================
# Configuração da Página
# ==========================

UI.configure_page()

if "history" not in st.session_state:
    st.session_state.history = []

UI.sidebar()
UI.header()
UI.show_history()


# ==========================
# Campo de Pesquisa
# ==========================

username = UI.search_box()


if UI.search_button():

    if not username:

        st.warning("Digite um usuário do GitHub.")

        st.stop()

    # ==========================
    # Buscar usuário
    # ==========================

    user = GitHubAPI.get_user(username)

    if user is None:

        st.error("Usuário não encontrado.")

        st.stop()

    # ==========================
    # Buscar Repositórios
    # ==========================

    repos = GitHubAPI.get_repositories(username)

    if repos is None:

        st.error("Erro ao buscar repositórios.")

        st.stop()

    # ==========================
    # Histórico
    # ==========================

    if username not in st.session_state.history:

        st.session_state.history.append(username)

    # ==========================
    # Formatar usuário
    # ==========================

    data = Formatter.format_user(user)

    st.write(data["created_at"])

    

    account_age = Analytics.account_age(
        data["created_at"]
    )

    # ==========================
    # Estatísticas
    # ==========================

    stats = Statistics.generate(repos)

    # ==========================
    # Interface
    # ==========================

    UI.show_profile(
        data,
        account_age
    )

    UI.show_metrics(
        data,
        stats
    )

    UI.show_best_repository(
        stats
    )

    UI.show_graphs(
        stats,
        repos
    )

    UI.show_table(
        stats
    )

    UI.show_statistics(
        stats
    )

    UI.show_export(
        username,
        repos
    )


# ==========================
# Rodapé
# ==========================

UI.footer()