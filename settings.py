from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = '0.0.0.0'
    DB_PORT: int = 15432
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    DB_NAME: str = 'pomodoro'

    CACHE_HOST: str = '0.0.0.0'
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0