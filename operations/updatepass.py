from db.dboperation import Operation
from rich.console import Console
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".passwdsl.env")
console = Console()


def update_credential(platform_name: str, passwd: str):
    """display all credentials 
    """
    dbname = os.getenv('DBNAME')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    try:
        with Operation(dbname=dbname, host=host, user=user, password=password, port=port) as cur:
            cur.execute(
                "UPDATE public.allpasswds SET passwd = %s WHERE platform = %s RETURNING id", (passwd, platform_name,))

            result = cur.fetchone()
            if not result:  # If data does not exist
                console.print(
                    f"[red]There is no password detected in database with platform name[/red] '{platform_name}'\n")
                return

            console.print(
                f"[bold cyan]Password updation for platform[/bold cyan] '{platform_name}'")
            console.print(
                f"[bold blue]Password of[/bold blue] '{platform_name}' [bold blue]has been successfully updated![/bold blue]")
            print()
    except Exception:
        console.print("""
Failed to display your credentials, it may be cause by following reasons:
1. You did not created table in your database.
2. PostgreSQL service is not running.
3. Database does not exist.\n
""")
