from db.database import Database
from rich.console import Console
from rich.table import Table
from psycopg2 import sql
from .connection import DataBaseConfig
from config import read

console = Console()


def update_credential(platform_name: str, password: str):
    """display all credentials 
    """
    platform_name = platform_name.strip()
    password = password.strip()

    if not platform_name or not password:
        console.print("[bold red]Platform and new password both are required.[/bold red]\n")
        return

    config = read()
    dbconfig = config["passwdsl"]["database"]

    dbname = dbconfig["dbname"]
    host = dbconfig["host"]
    port = dbconfig["port"]
    user = dbconfig["user"]
    dbpassword = dbconfig["password"]
    table = dbconfig["table"]
    id_col, platform_col, password_col = dbconfig["columns"]

    if not table:
        console.print("[bold red]Table name is missing in config.yaml.[/bold red]\n")
        return

    conn_check = DataBaseConfig(dbname=dbname, host=host, user=user, password=dbpassword, port=port).check_db()
    if isinstance(conn_check, tuple):
        console.print(f"[bold red]Database check failed: {conn_check[1]}[/bold red]\n")
        return

    try:
        with Database(dbname=dbname, host=host, user=user, password=dbpassword, port=port) as cur:
            cur.execute(
                sql.SQL("UPDATE public.{} SET {} = %s WHERE {} = %s RETURNING {}, {}, {}").format(
                    sql.Identifier(table),
                    sql.Identifier(password_col),
                    sql.Identifier(platform_col),
                    sql.Identifier(id_col),
                    sql.Identifier(platform_col),
                    sql.Identifier(password_col)
                ),
                (password, platform_name)
            )

            result = cur.fetchone()
            if not result:  # If data does not exist
                console.print(
                    f"[bold yellow]No credential found for[/bold yellow] [cyan]{platform_name}[/cyan].\n")
                return

            result_table = Table(title="Credential Updated", show_header=True, show_lines=True)
            result_table.add_column("Id")
            result_table.add_column("Platform")
            result_table.add_column("Password")
            result_table.add_row(str(result[0]), f"[cyan]{result[1]}[/cyan]", f"[bold]{result[2]}[/bold]")

            print()
            console.print(result_table)
            print()
    except Exception as e:
        console.print(f"[bold red]Failed to update credential.[/bold red] {e}\n")
