from pathlib import Path

import yaml

   
def load_settings() -> dict:
    settings_path = Path.home() / ".chatbot"/ "settings.yaml"
    settings_dict =  yaml.safe_load(settings_path.read_text())
    return settings_dict


