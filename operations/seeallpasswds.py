from db.dboperation import Operation
from rich.console import Console
from dotenv import load_dotenv
import os

load_dotenv()
console = Console()


def display_credentials():
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
    except Exception as e:

        console.print(e)
        console.print("""
Failed to display your credentials, it may be cause by following reasons:
1. You did not created table in your database.
2. Wrong command syntax.\n
                      """)
