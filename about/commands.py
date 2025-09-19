from style.text_style import text_styles


def all_commands():
    cmds = f"""                                                                                                                                                                        
{text_styles.bold}passwds{text_styles.reset}                                                             See your all credentials                                                      
{text_styles.bold}passwd -platform 'platform_name'{text_styles.reset}                                    See password for specific platform                                                       
{text_styles.bold}passadd -cred 'password' -of 'platform_name'{text_styles. reset}                        Add credentials (password) with platform name 
{text_styles.bold}passrm  -cred 'password' -of 'platform_name'{text_styles.reset}                        Remove your credentials by specifing 'pass' and their 'plaform_name'                                                                 
{text_styles.bold}passup  -new 'password' -of 'platform_name'{text_styles.reset}                         Update your credentials by just specifing their 'platform_name'
    """
    print(cmds)
