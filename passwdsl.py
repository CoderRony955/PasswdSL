from rich.console import Console
from about.welcome import welcome
from about.commands import all_commands
import handlers

console = Console()


def main():
    try:
        welcome()  # Show welcome message first time

        while True:
            try:
                user = input(">_ ")
                if user == "help" or user == "h":
                    all_commands()
                elif user.split()[0] == "passadd" and "-cred" in user.split() and "-of" in user.split():
                    handlers.handle_commands(usercmd=user)
                elif user.split()[0] == "passup" and "-new" in user.split() and "-of" in user.split():
                    handlers.handle_commands(usercmd=user)
                elif user.split()[0] == "passrm" and "-of" in user.split():
                    handlers.handle_commands(usercmd=user)
                elif user == "passwds":
                    handlers.handle_commands(usercmd=user)
                elif user.split()[0] == "passwd" and user.split()[1] == "-of":
                    handlers.handle_commands(usercmd=user)
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
