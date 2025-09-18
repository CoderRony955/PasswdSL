from rich.console import Console
from about.welcome import welcome
from about.commands import all_commands

console = Console()


def main():
    welcome()  # Show welcome message

    while True:
        user = input(">_ ")
        if user == "help" or user == "h":
            all_commands()
        elif user == "":
            continue
        elif user == "q" or user == "exit" or user == "quit":
            console.print("[bold italic]see ya![/bold italic]")
            break
        else:
            console.print(
                "\n[bold red]Unknown command![/bold red] Use 'help' to see all available commands\n")


if __name__ == "__main__":
    main()
