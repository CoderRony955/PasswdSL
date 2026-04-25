from rich.console import Console
from rich.prompt import Prompt
import psycopg2
import time
import yaml
import sys
import os

# database configurations
from config import (
    database_host,
    database_port,
    database_password,
    database_user,

)

console = Console()


class DataBaseConfig:
    """Database connection operations
    """

    def __init__(self, dbname: str, host: str, user: str, password: str, port: str):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port

        # reaad config file
        with open("./config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    def connect_to_db(self):
        try:
            psycopg2.connect(
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

    def save_to_config(self, db: str, host: str, port: str, user: str, password: str):
        """save database credentials to config file

        Args:
            db (str): Database name
            host (str): Host
            user (str): User
            password (str): Database password
            port (str): Port
        """
        self.config["passwdsl"]["database"]["dbname"] = db
        self.config["passwdsl"]["database"]["host"] = host
        self.config["passwdsl"]["database"]["port"] = port
        self.config["passwdsl"]["database"]["user"] = user
        self.config["passwdsl"]["database"]["password"] = password
        self.connect_to_db()

        # save to config file
        with open("./config.yaml", "w") as file:
            yaml.dump(self.config, file)

        console.print(
            "\n✅ Database connected and all credentials for database connection has been successfully saved! Now just restart Passwdsl to continue.\n", style="bold green")
        sys.exit(0)

    def check_db(self):
        try:
            # check database connection
            with console.status("[bold green]Checking Database Connection..."):
                for _ in range(3):
                    time.sleep(0.5)

            # check if .env already exist or not if not then create first
            if not os.path.exists("./config.yaml"):
                console.print(
                    "[red]configuration file is not found! Please create new one with proper required configs.[/red]\n")
                sys.exit(1)

            # if config file exist then check all database login credentials for connection
            if not database_host or not database_password or not database_port or not database_user:
                console.print(
                    "\n[bold yellow]Database is not connected and some of them Database Credentials are missing or added wrong credentials information, please provide your database login credentials again for smooth login:[/bold yellow]\n\n")

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

                    # Save all database connection credentials to config file
                self.save_to_config(db=dbname, host=host,
                                    port=port, user=user, password=dbpassword)
            else:
                # Healthy startup path should stay quiet so intro/login UI renders first.
                self.connect_to_db()

        except Exception as e:
            return (False, str(e))
