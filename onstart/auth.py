from rich.console import Console
import maskpass
import yaml
import sys
import os

console = Console()


class Auth:
    def __init__(self):
        if not os.path.exists("./config.yaml"):
            console.print(
                "[red]configuration file \'config.yaml\' is not found! Please create new one to continue")
            return

        # read config file
        with open("./config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    def createNewPass(self):
        try:
            while True:
                user_input = maskpass.askpass(
                    prompt="Enter the New Password: ", mask="*")
                if not user_input:
                    continue

                # add to config file
                self.config["passwdsl"]["login_pass"] = user_input

                # write back to config file
                with open("./config.yaml", "w") as file:
                    yaml.dump(self.config, file)
                break
        except Exception as e:
            return (False, str(e))

    def AskForPass(self):
        try:
            max_retry = 5
            retry = 0
            while True:
                if retry == max_retry:
                    console.print(
                        "[bold red]Unable to login after Max retries![/bold red]")
                    sys.exit(1)

                user_input = maskpass.askpass(
                    prompt="Enter the Password to login: ", mask="*"
                )
                if not user_input:
                    continue

                if user_input == self.config["passwdsl"]["login_pass"]:
                    console.print(
                        "[bold green]Login Successful![/bold green]\n")
                    break
                else:
                    console.print(
                        "[red]Wrong password! Please try again.[/red]\n")
                    retry += 1
        except Exception as e:
            return (False, str(e))
