from pydantic import Field, SecretStr, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    user_name: str = Field()
    password: SecretStr = Field()
    host: str
    port: PositiveInt
    database_name: str = Field()
    db_echo: bool = Field()
    database_url_test: str = Field()
    database_url_prod: str = Field()
    SECRET_JWT_CODE: str 
    
    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8')


app_settings = Settings()