from rich.console import Console
from .auth import Auth
import yaml
import sys
import os

console = Console()
auth = Auth()


class Do:
    def __init__(self):
        if not os.path.exists("./config.yaml"):
            console.print(
                "[red]configuration file \'config.yaml\' is not found! Please create new one to continue")
            return

        # read config file
        with open("./config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    def introduction(self):
        intro = f"""                                                 
[bold]PasswdSL[/bold] Console is your personal command-line password manager, backed by a secure [cyan]PostgreSQL[/cyan] database.

[italic]
✔  Securely store and manage your passwords locally  
✔  Perform full CRUD operations [bold](Add Pass, See Pass, Update Pass, Delete Pass)[/bold]  
✔  Keep all your credentials organized and accessible  
✔  No external servers — your data stays with you[/italic] 

Take control of your digital security with simplicity and power.  
Type a command to get started, or enter [green]\'help\'[/green] to see available options.
                """
        # read ./ascii_text.txt for ASCII styled passwdsl text
        with open("./onstart/ascii_text.txt", "r") as file:
            ascii_txt = file.read()

        # display
        console.print(f"[green]{ascii_txt}[/green]")
        print()  # for spacing
        console.print(intro)

    def login(self):
        try:
            if not self.config["passwdsl"]["login_pass"]:
                create_new_pass = auth.createNewPass()
                if isinstance(create_new_pass, tuple):
                    console.print(f"[red]{create_new_pass[1]}[/red]\n")
                    sys.exit(1)

            # if password already exist then directly ask for pass to login
            login_with_pass = auth.AskForPass()
            if isinstance(login_with_pass, tuple):
                console.print(f"[red]{login_with_pass[1]}[/red]\n")
                sys.exit(1)
        except Exception as e:
            return (False, str(e))
