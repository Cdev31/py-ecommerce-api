from .config_type import ConfigType
import os


config: ConfigType = {
    'db_url': os.getenv('DB_URL') or ''
}

