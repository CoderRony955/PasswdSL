from db.dboperation import Operation
from rich.console import Console
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".passwdsl.env")
console = Console()


def display_credentials(dbname, host, user, password, port):
    """display all credentials 
    """
    dbname = os.getenv('DBNAME')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    try:
        with Operation(dbname=dbname, host=host, user=user, password=password, port=port) as cur:
            cur.execute("SELECT * FROM public.allpasswds")
            for creds in cur.fetchall():
                console.print(
                    f"{creds}")
            print()
    except Exception:
        console.print("""
Failed to display your credentials, it may be cause by following reasons:
1. You did not created table in your database.
2. PostgreSQL service is not running.\n
""")
