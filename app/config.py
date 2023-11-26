from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mysql_root_password:str
    mysql_database:str
    mysql_user:str
    mysql_password:str
    mysql_port:int

    def get_database_url(self):
        return f"mysql+mysqlconnector://{self.mysql_user}:{self.mysql_password}@db:{self.mysql_port}/{self.mysql_database}"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()