import yaml


def get_config(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def get_email_config():
    credentials = get_config("config.yaml")['email']
    USER = credentials['USER']
    PASSWORD = credentials['PASSWORD']
    HOST = credentials['HOST']
    return USER, PASSWORD, HOST


def get_mongodb_config():
    credentials = get_config("config.yaml")['mongodb']
    USER = credentials['USER']
    PASSWORD = credentials['PASSWORD']
    CONNECTION_URL = credentials["CONNECTION_URL"].format(USER=USER, PASSWORD=PASSWORD)
    return CONNECTION_URL
