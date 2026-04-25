from rich.console import Console
from onstart.on_start import Do
from onstart.commands import all_commands
from operations.connection import DataBaseConfig
from command_handlers import Handler
import sys

from config import (
    database_host,
    database_name,
    database_password,
    database_port,
    database_user
)

console = Console()
onstart = Do()
handler = Handler()
dbconfig = DataBaseConfig(dbname=database_name, host=database_host,
                          user=database_user, password=database_password, port=database_port)


def main():
    try:
        onstart.introduction()  # introduction
        login = onstart.login()
        if isinstance(login, tuple):
            console.print(f"[red]{login}[/red]\n")
            sys.exit(1)

        dbconfig.check_db()  # database connection check
        while True:
            try:
                user = input(">_ ")

                # Command to display all available commands
                if user == "help" or user == "h":  # Help command
                    all_commands()

                # Command to add password in database
                elif user.lower().startswith("passadd"):
                    passaddcmd = user.split()
                    if len(passaddcmd) < 5:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passadd[/bold] [red]command[/red]\npassadd -cred 'password' -of 'platform_name' [cyan]<- Please use this valid syntax.[/cyan]\n")
                        continue

                    elif passaddcmd[1] != "-cred" or passaddcmd[3] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passadd[/bold] [red]command[/red]\npassadd -cred 'password' -of 'platform_name' [cyan]<- Please use this valid syntax.[/cyan]\n")
                        continue

                    # move to operation to add password to database
                    addpass = handler.for_adding_password(command=passaddcmd)
                    if isinstance(addpass, tuple):
                        console.print(f"[red]{addpass[1]}[/red]\n")

                # Command to updated password
                elif user.lower().startswith("passup"):
                    passupcmd = user.split()
                    if len(passupcmd) < 5:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passup[/bold] [red]command[/red]\npassup -new 'password' -of 'platform_name' [cyan]<- Please use this valid syntax to update any specific password.[/cyan]\n")
                        continue

                    elif passupcmd[1] != "-new" or passupcmd[3] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passup[/bold] [red]command[/red]\npassup -new 'password' -of 'platform_name' [cyan]<- Please use this valid syntax to update any specific password.[/cyan]\n")
                        continue

                    # move to operation to update existing password
                    updatepass = handler.for_updating_password(
                        command=passupcmd)
                    if isinstance(updatepass, tuple):
                        console.print(f"[red]{updatepass[1]}[/red]\n")

                # Command to remove password from database
                elif user.lower().startswith("passrm"):
                    delpasscmd = user.split()
                    if len(delpasscmd) < 3:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passrm[/bold] [red]command[/red]\npassrm -of 'platform_name' [cyan]<- Please use this valid syntax to remove your any specifc credential (password) from database.[/cyan]\n")
                        continue

                    elif delpasscmd[1] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passrm[/bold] [red]command[/red]\npassrm -of 'platform_name' [cyan]<- Please use this valid syntax to remove your any specifc credential (password) from database.[/cyan]\n")
                        continue

                    # move to operation to deleting existing password
                    delpasscmd = handler.for_deleting_password(
                        command=delpasscmd)
                    if isinstance(delpasscmd, tuple):
                        console.print(f"[red]{delpasscmd[1]}[/red]\n")

                # Command to display all saved passwords
                elif user.lower() == "passwds":
                    handler.for_command_see_all_password()

                # Command to display specific password of any platform
                elif user.lower().startswith("passwd"):
                    specificpasscmd = user.split()
                    if len(specificpasscmd) < 3:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passwd[/bold] [red]command[/red]\npasswd -of 'platform_name' [cyan]<- Please use this valid syntax to see specific password.[/cyan]\n")
                        continue

                    elif specificpasscmd[1] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passwd[/bold] [red]command[/red]\npasswd -of 'platform_name' [cyan]<- Please use this valid syntax to see specific password.[/cyan]\n")
                        continue

                    # move to operation to display specific existing password
                    specificpasscmd = handler.for_displaying_specific_password(
                        command=specificpasscmd)
                    if isinstance(specificpasscmd, tuple):
                        console.print(f"[red]{specificpasscmd[1]}[/red]\n")

                # Command to exit from 'PasswdSL' console
                elif user.lower() == "q" or user.lower() == "exit" or user.lower() == "quit":
                    console.print(
                        "[bold italic green]see ya![/bold italic green]")
                    break
                else:
                    console.print(
                        "\n[bold red]Wrong command![/bold red] Please use exact command without any extra single character or use 'help' to see all available commands\n")
            except Exception as e:
                console.print(f"[bold red]{e}[/bold red]")
                continue

    except KeyboardInterrupt:
        console.print("\n[bold italic green]see ya![/bold italic green]")


if __name__ == "__main__":
    main()
