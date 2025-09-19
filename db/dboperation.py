from rich.console import Console
import psycopg2
import time

console = Console()


class Operation:
    def __init__(self, dbname, host, user, password, port):
        self.dbname = dbname
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.conn = None
        self.cur = None


    def __enter__(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
            return self.cur
        except Exception as e:
            print(e)
            console.print(
                "[bold red]Failed to connect Database![/bold red]")
            

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()

    # try:
    #     with ConnectDb("mypasswds", "localhost", "postgres", "raunaksh955", "5432") as cur:
    #         # Example of how to use the cursor
    #         cur.execute("DELETE FROM public.allpasswds WHERE id = 1")
    # except Exception as e:
    #     console.print(f"[bold red]Something went wrong: {e}[/bold red]")
