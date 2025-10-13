from rich.console import Console
from about.welcome import welcome
from about.commands import all_commands
import handlers

console = Console()


def main():
    try:
        welcome()  # Display welcome message

        while True:
            try:
                user = input(">_ ")
                # Command to display all available commands
                if user == "help" or user == "h":  # Help command
                    all_commands()

                # Command to add password in database
                elif user.split()[0] == "passadd":
                    passaddcmd = user.split()
                    if len(passaddcmd) < 5:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passadd[/bold] [red]command[/red]\npassadd -cred 'password' -of 'platform_name' [cyan]<- Please use this valid syntax.[/cyan]\n")
                        continue

                    elif passaddcmd[1] != "-cred" or passaddcmd[3] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passadd[/bold] [red]command[/red]\npassadd -cred 'password' -of 'platform_name' [cyan]<- Please use this valid syntax.[/cyan]\n")
                        continue

                    handlers.handle_commands(usercmd=user)

                # Command to updated password
                elif user.split()[0] == "passup":
                    passupcmd = user.split()
                    if len(passupcmd) < 5:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passup[/bold] [red]command[/red]\npassup -new 'password' -of 'platform_name' [cyan]<- Please use this valid syntax to update any specific password.[/cyan]\n")
                        continue

                    elif passupcmd[1] != "-new" or passupcmd[3] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passup[/bold] [red]command[/red]\npassup -new 'password' -of 'platform_name' [cyan]<- Please use this valid syntax to update any specific password.[/cyan]\n")
                        continue

                    handlers.handle_commands(usercmd=user)

                # Command to remove password from database
                elif user.split()[0] == "passrm":
                    passrmcmd = user.split()
                    if len(passrmcmd) < 3:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passrm[/bold] [red]command[/red]\npassrm -of 'platform_name' [cyan]<- Please use this valid syntax to remove your any specifc credential (password) from database.[/cyan]\n")
                        continue

                    elif passrmcmd[1] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passrm[/bold] [red]command[/red]\npassrm -of 'platform_name' [cyan]<- Please use this valid syntax to remove your any specifc credential (password) from database.[/cyan]\n")
                        continue

                    handlers.handle_commands(usercmd=user)

                # Command to display all passwords
                elif user == "passwds":
                    handlers.handle_commands(usercmd=user)

                # Command to display specific password of any platform
                elif user.split()[0] == "passwd":
                    passwdcmd = user.split()
                    if len(passwdcmd) < 3:
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passwd[/bold] [red]command[/red]\npasswd -of 'platform_name' [cyan]<- Please use this valid syntax to see specific password.[/cyan]\n")
                        continue

                    elif passwdcmd[1] != "-of":
                        console.print(
                            f"{user} [red]<- Wrong syntax of using[/red] [bold]passwd[/bold] [red]command[/red]\npasswd -of 'platform_name' [cyan]<- Please use this valid syntax to see specific password.[/cyan]\n")
                        continue

                    handlers.handle_commands(usercmd=user)

                # Command to exit from 'PasswdSL' console
                elif user == "q" or user == "exit" or user == "quit":
                    console.print("[bold italic]see ya![/bold italic]")
                    break
                else:
                    console.print(
                        "\n[bold red]Wrong command![/bold red] Use 'help' to see all available commands\n")
            except Exception:
                continue

    except KeyboardInterrupt:
        console.print("[bold italic]see ya![/bold italic]")


if __name__ == "__main__":
    main()
