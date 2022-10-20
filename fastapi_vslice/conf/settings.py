from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str
    db_test_url: str

    session_auto_commit: bool = False
    session_auto_flush: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
