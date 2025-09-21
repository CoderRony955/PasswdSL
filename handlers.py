from rich.console import Console
from rich.prompt import Prompt
from dotenv import load_dotenv, dotenv_values
from operations import (
    addpass,
    seeallpasswds,
    see_specific_pass,
    delpass,
    updatepass
)
import psycopg2
import random
import time
import os


load_dotenv()
console = Console()

success_messages = [
    "All systems go 🚀",
    "Connection is smooth like butter 🧈",
    "Database vibes are good ✨",
    "We’re in! 🔑",
    "DB says hello 👋",
    "Connection locked and loaded 🔒➡️🔓",
    "Pipeline is flowing 💧",
    "Synced and ready 🎯",
    "DB handshake successful 🤝",
    "Data highway is clear 🛣️",
    "Connection feels awesome 😎",
    "Mission accomplished ✅"
]


class Connectdb:
    """connect to database
    """

    def __init__(self, dbname, host, user, password, port):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def connect_to_db(self):
        try:
            conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.db_creds = [self.dbname, self.host,
                             self.user, self.password, self.port]
            return
        except Exception as e:
            console.print(
                f"\n[bold red]Database connection failed![/bold red]\nReason: {e}")

    def pass_db_credentials(self):
        return self.db_creds


def create_env(DB: str, HOST: str, USER: str, PASS: str, PORT: str):
    """create .env file to save database connection credentials

    Args:
        DB (str): Database name
        HOST (str): Host
        USER (str): User
        PASS (str): Database password
        PORT (str): Port
    """
    conndb = Connectdb(dbname=DB, host=HOST, user=USER,
                       password=PASS, port=PORT)
    conndb.connect_to_db()

    file_blueprint = [f'DBNAME={conndb.pass_db_credentials()[0]}', f'HOST={conndb.pass_db_credentials()[1]}',
                      f'USER={conndb.pass_db_credentials()[2]}', f'PASSWORD={conndb.pass_db_credentials()[3]}', f'PORT={conndb.pass_db_credentials()[4]}']

    with open("./.env", "w") as file:
        for line in file_blueprint:
            file.writelines(f"{line}\n")
    console.print(
        "\n✅ Database connected and all credentials for database connection has been successfully saved!\n", style="bold green")


# Main handler to handle all commands
def check_db():
    try:
        # check database connection
        with console.status("[bold green]Checking Database Connection..."):
            for _ in range(3):
                time.sleep(0.5)

        # check if .env already exist or not if not then create first
        if os.path.exists("./.env"):
            with open("./.env", "r") as file:
                console.print(
                    f"\n{random.choice(success_messages)}", style="bold green")
            return True
        else:
            console.print("\n[bold yellow]Database is not connected and Database Credentials file '.env' is missing, please specify credentials to connect database and save Database Credentials to a file:[/bold yellow]\n\n")

            dbname = Prompt.ask(
                "Enter your [cyan]postgres[/cyan] [bold]database name[/bold]: ")
            host = Prompt.ask("Enter the [bold]host[/bold]: ")
            user = Prompt.ask("Enter [bold]database user[/bold]: ")
            dbpassword = Prompt.ask(
                "Enter your [bold]database password[/bold]: ")
            port = Prompt.ask("Enter the [bold]port[/bold]: ")

            with console.status("\n[bold green]Connecting to a Database...\n"):
                for _ in range(3):
                    time.sleep(0.5)
            # create .env file to save all database connection credentials
            create_env(DB=dbname, HOST=host, USER=user,
                       PASS=dbpassword, PORT=port)
            return True

    except Exception:
        return False


# Handle 'passadd' command to add credentials in database
def passadd_handler(command: list[str]):
    print(f"Password: {command[2]}")
    print(f"For: {command[4]}\n")
    try:
        password = command[2]
        platform = command[4]
        addpass.add_credential(platform, password)
    except Exception as e:
        console.print(e)
        return

# Handle 'passwsds' command to display all credentials


def passwds_cmd_handler():
    try:
        config = dotenv_values(".env")
        dbname = config.get('DBNAME')
        host = config.get('HOST')
        user = config.get('USER')
        password = config.get('PASSWORD')
        port = config.get('PORT')
        seeallpasswds.display_credentials(dbname, host, user, password, port)
    except Exception as e:
        console.print(e)
        return


# Handle 'passwsd' command to display specific credential


def passwd_cmd_handler(command: list[str]):
    try:
        see_specific_pass.display_specific_credential(command[2])
    except Exception as e:
        console.print(e)
        return


# Handle 'passrm' command to remove or delete credentials


def passrm_cmd_handler(command: list[str]):
    try:
        delpass.del_credential(command[2])
    except Exception as e:
        console.print(e)
        return


# Handle 'passup' command to update credentials


def passup_cmd_handler(command: list[str]):
    try:
        updatepass.update_credential(command[4], command[2])
    except Exception as e:
        console.print(e)
        return

# Handle all commands


def handle_commands(usercmd: str):
    try:
        # to handle 'adding password' operations
        if check_db():
            if usercmd.split()[0] == "passadd":
                passadd_handler(command=usercmd.split())
            elif usercmd.split()[0] == "passwds":
                passwds_cmd_handler()
            elif usercmd.split()[0] == "passrm":
                passrm_cmd_handler(command=usercmd.split())
            elif usercmd.split()[0] == "passup":
                passup_cmd_handler(command=usercmd.split())
            elif usercmd.split()[0] == "passwd":
                passwd_cmd_handler(command=usercmd.split())
    except Exception as e:
        console.print(e)
