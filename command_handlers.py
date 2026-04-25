from rich.console import Console
from typing import List
from operations import (
    connection,
    deletepass,
    see_all_passwords,
    addpass,
    updatepass,
    see_specific_pass
)

from config import (
    database_host,
    database_name,
    database_password,
    database_port,
    database_user
)

dbconfig = connection.DataBaseConfig(dbname=database_name, host=database_host,
                                     user=database_user, password=database_password, port=database_port)

console = Console()


def removeCommas(text: str):
    final_text = ""
    for i in text:
        if i == "\'" or i == "\"":
            continue
        else:
            final_text += i
    return final_text


class Handler:
    @staticmethod
    def connection_check():
        db_conn = dbconfig.check_db()
        if isinstance(db_conn, tuple):
            console.print(f"[red]Something went wrong! {db_conn[1]}[/red]\n")
            return False
        return True

    @staticmethod
    def for_command_see_all_password():
        see_all_passwords.display(
            dbname=database_name,
            host=database_host,
            user=database_user,
            password=database_password,
            port=database_port
        )

    @staticmethod
    def for_adding_password(command: List[str]):
        try:
            password = ""
            platform = ""

            # extract password from command first
            for i in command[2:]:
                if "-of" in i:
                    break
                password += i

            # extract platform name from command
            for j in command[command.index('-of') + 1:]:
                platform += j

            # add password to database
            addpass.add_credential(platform_name=removeCommas(
                platform.lower()), password=removeCommas(password))
        except Exception as e:
            return (False, str(e))

    @staticmethod
    def for_updating_password(command: List[str]):
        try:
            password = ""
            platform = ""

            # extract password from command first
            for i in command[2:]:
                if "-of" in i:
                    break
                password += i

            # extract platform name from command
            for j in command[command.index('-of') + 1:]:
                platform += j

            # add password to database
            updatepass.update_credential(platform_name=removeCommas(
                platform.lower()), password=removeCommas(password))
        except Exception as e:
            return (False, str(e))

    @staticmethod
    def for_deleting_password(command: List[str]):
        try:
            platform = ""

            # extract platform name from command
            for j in command[command.index('-of') + 1:]:
                platform += j

            # add password to database
            deletepass.del_credential(
                platform_name=removeCommas(platform.lower()))
        except Exception as e:
            return (False, str(e))

    @staticmethod
    def for_displaying_specific_password(command: List[str]):
        try:
            platform = ""

            # extract platform name from command
            for j in command[command.index('-of') + 1:]:
                platform += j

            # add password to database
            see_specific_pass.display_specific_credential(
                platform_name=removeCommas(platform.lower()))
        except Exception as e:
            return (False, str(e))
