from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_user_name: str
    db_password: str
    db_name: str
    db_port: int


settings = Settings()
