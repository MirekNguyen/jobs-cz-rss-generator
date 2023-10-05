import json
import os


class Config:
    def __init__(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                self.data = json.load(f)
        else:
            config_default = "config/config_template.json"
            if os.path.exists(config_default):
                print(
                    f"{config_file} file not found. Using default values from {config_default}"
                )
                with open(config_default, "r") as f:
                    self.data = json.load(f)
            else:
                 raise FileNotFoundError(f"Config file '{config_default}' not found.")
