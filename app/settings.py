from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    user_name: str
    password: str
    db_name: str
    port: int


settings = Settings()



