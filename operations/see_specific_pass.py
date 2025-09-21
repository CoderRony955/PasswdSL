from db.dboperation import Operation
from rich.console import Console
from dotenv import load_dotenv
import os

load_dotenv()
console = Console()


def display_specific_credential(platform_name: str):
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
                "SELECT * FROM public.allpasswds WHERE platform = %s", (platform_name,))
            
            result = cur.fetchone()
            if not result: # If data does not exist 
                console.print(f"[red]There is no password detected in database with platform name[/red] '{platform_name}'\n")
                return
            
            console.print(f"""
[bold]id:[/bold] {result[0]}
[bold]platform:[/bold] {result[1]}
[bold]password:[/bold] [cyan]{result[2]}[/cyan]
                          """)
            print()
    except Exception:
        console.print("""
Failed to display your credentials, it may be cause by following reasons:
1. You did not created table in your database.
2. PostgreSQL service is not running.
3. Database does not exist.\n
""")
