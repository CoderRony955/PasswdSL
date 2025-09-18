from style.text_style import text_colors, text_styles


def welcome():
    des = f"""{text_colors.green}
    ____                               _______ __ 
   / __ \\____ ____________      ______/ / ___// / 
  / /_/ / __ `/ ___/ ___/ | /| / / __  /\\__ \\/ /  
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ /___/ / /___
/_/    \\__,_/____/____/ |__/|__/\\__,_//____/_____/{text_colors.reset}
                                                    
{text_styles.bold}
PasswdSL{text_styles.reset} Console is your personal command-line password manager, backed by a secure {text_colors.cyan}PostgreSQL{text_colors.reset} database.

{text_styles.italic}
✔  Securely store and manage your passwords locally  
✔  Perform full CRUD operations (Create, Read, Update, Delete)  
✔  Keep all your credentials organized and accessible  
✔  No external servers — your data stays with you{text_styles.reset}  

Take control of your digital security with simplicity and power.  
Type a command to get started, or enter {text_colors.green}'help'{text_colors.reset} to see available options.
    """
    print(des)
