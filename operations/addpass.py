from db.dboperation import Operation
from rich.console import Console
from dotenv import load_dotenv
import os

load_dotenv()
console = Console()


def add_passwd(platform_name: str, passwd: str):
    """add credentials (passwords)

    Args:
        platform_name (str, required): platform name of that password that you are adding.
        passwd (str, required): password. 
    """
    dbname = os.getenv('DBNAME')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    try:
        with Operation(dbname=dbname, host=host, user=user, password=password, port=port) as cur:
            cur.execute("INSERT INTO public.allpasswds (platform, passwd) VALUES (%s, %s) RETURNING id",
                        (platform_name, passwd,))
            console.print(
                f"[bold green]Successfully added password for {platform_name}![/bold green]\n")
    except Exception as e:

        console.print(e)
        console.print("""
Failed to add your credentials in database, it may be cause by following reasons:
1. You did not created table in your database.
2. You did not added specific columns. (Columns must be like that -> | id | platform_name | passwd | with same names and same number of columns, no additional column required)
3. Wrong command syntax.\n
                      """)
