import yaml

def get_configs():
    with open("config.yaml", "r") as stream:
        try:
            data = yaml.safe_load(stream)["database"]
            username = data["username"]
            password = data["password"]
            dbname = data["dbname"]
        except yaml.YAMLError as exc:
            print(exc)
    return username, password, dbname

def get_app_data():
    with open("config.yaml", "r") as stream:
        try:
            data = yaml.safe_load(stream)["app"]
            secret_key = data["secret_key"]
        except yaml.YAMLError as exc:
            print(exc)
    return secret_key