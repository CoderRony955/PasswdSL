import yaml

# read config file
with open("./config.yaml", "r") as file:
    config = yaml.safe_load(file)

# database credentials ---------------------------

# name
database_name = config["passwdsl"]["database"]["dbname"]

# host
database_host = config["passwdsl"]["database"]["host"]

# port
database_port = config["passwdsl"]["database"]["port"]

# password
database_password = config["passwdsl"]["database"]["password"]

# user
database_user = config["passwdsl"]["database"]["user"]

# table
table = config["passwdsl"]["database"]["table"]

# columns
columns = {
    "id": config["passwdsl"]["database"]["columns"][0],
    "platform": config["passwdsl"]["database"]["columns"][1],
    "password": config["passwdsl"]["database"]["columns"][2]
}


def read():
    """read configuration file adn return config data
    """
    with open("./config.yaml", "r") as file:
        config = yaml.safe_load(file)
        return config

