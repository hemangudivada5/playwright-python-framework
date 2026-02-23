import json
import os


def config_reader():
    #Reading of env variable
    env = os.getenv("ENV","qa")

    with open("config/config.json") as f:
        config = json.load(f)

    if env not in config:
        raise Exception(f"Environment '{env}' not found in config.json")

    return config[env]