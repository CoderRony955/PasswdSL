from rich.table import Table
from rich.console import Console

console = Console()


def all_commands():
    commands = {
        "passwds": "See your all passwords",
        "passwd -of \'platform_name\'": "See password for specific platform",
        "passadd -cred \'password\' -of \'platform_name\'": "Add credentials (passwords) with platform name",
        "passrm -of \'platform_name\'": "Remove your credentials by specifying their \'platform_name\'",
        "passup -new \'password\' -of \'platform_name\'": "Update your credentials by just specifying their \'platform_name\'"
    }
    # commands table
    table = Table(show_lines=True)
    table.add_column("Commands")
    table.add_column("Purpose")
    
    print()
    for command, purpose in commands.items():
        table.add_row(f"[cyan]{command}[/cyan]", f"[bold]{purpose}[/bold]")
        
    # display commands 
    console.print(table)
    print()
