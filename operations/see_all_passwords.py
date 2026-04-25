from db.database import Database
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from .connection import DataBaseConfig
import yaml
import sys

from config import table, read

console = Console()
config = read()


def display(dbname: str, host: str, user: str, password: str, port: str):
    """display all credentials (passwords) 
    """
    dbconfig = DataBaseConfig(dbname=dbname, host=host,
                              user=user, password=password, port=port)
    try:
        check_conn = dbconfig.check_db()
        if isinstance(check_conn, tuple):
            console.print(
                f"[red]Something went wrong! {check_conn[1]}[/red]\n")

        # if table name is None
        if not table:
            while True:
                table_name = Prompt.ask(
                    "[italic]Enter the Table in which all passwords are stored[/italic] ")
                if not table_name:
                    continue

                # save table name to config
                config["passwdsl"]["database"]["table"] = table_name
                with open("./config.yaml", "w") as file:
                    yaml.dump(config, file)
                console.print(
                    "[bold green]Saved to config! Now restart Passwdsl to continue.[/bold green]\n")
                sys.exit(0)

        with Database(dbname=dbname, host=host, user=user, password=password, port=port) as cur:
            cur.execute(f"SELECT * FROM public.{table}")

            # table for displaying passwords in proper structured format
            passwords_table = Table(show_lines=True)
            passwords_table.add_column("Id")
            passwords_table.add_column("Platform")
            passwords_table.add_column("Password")

            print()
            for creds in cur.fetchall():
                passwords_table.add_row(
                    f"{creds[0]}", f"[cyan]{creds[1]}[/cyan]", f"[bold]{creds[2]}[/bold]")
            console.print(passwords_table)
            print()
    except Exception as e:
        console.print(
            f"[bold red]Failed to display your credentials. {e}[/bold red]\n")
