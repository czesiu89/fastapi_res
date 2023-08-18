from pydantic import BaseSettings, Field


class Config(BaseSettings):
    ENV: str = Field(env="ENV", default="development")
    LOG_LEVEL: str = Field(env="LOG_LEVEL", default="INFO")
    UVICORN_LOG_LEVEL: str = Field(env="UVICORN_LOG_LEVEL", default="info")
    SERIALIZE_LOG: bool = Field(env="SERIALIZE_LOG", default=False)
    APP_HOST: str = Field(env="APP_HOST", default="0.0.0.0")
    APP_PORT: int = Field(env="APP_PORT", default=9000)


config = Config()
