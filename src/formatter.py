from datetime import datetime


class Formatter:

    @staticmethod
    def format_number(number):
        """
        Formata números grandes.

        Ex:
        1200 -> 1.200
        35000 -> 35.000
        """

        if number is None:
            return "0"

        return f"{number:,}".replace(",", ".")

    @staticmethod
    def format_date(date):
        """
        Converte:

        2018-04-15T13:52:10Z

        para

        15/04/2018
        """

        if not date:
            return "-"

        date = datetime.strptime(
            date,
            "%Y-%m-%dT%H:%M:%SZ"
        )

        return date.strftime("%d/%m/%Y")

    @staticmethod
    def format_user(user):
        """
        Organiza todas as informações do usuário
        em um único dicionário.
        """

        return {

            "login": user.get("login"),

            "name": user.get("name") or user.get("login"),

            "avatar": user.get("avatar_url"),

            "bio": user.get("bio") or "Sem biografia.",

            "company": user.get("company") or "-",

            "location": user.get("location") or "-",

            "profile": user.get("html_url"),

            "followers": user.get("followers", 0),

            "repositories": user.get("public_repos", 0),

            "created_at": user.get("created_at")
            

        }