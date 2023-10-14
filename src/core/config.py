import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "api/v1"
    SERVER_NAME: str
    PROJECT_NAME: str = "Translator AI"

    FROM_MULTI_TO_ENG_MODEL_PATH: str = "/code/src/ml_model/opus-mt-mul-en.pkl"

    class Config:
        case_sensitive = True

settings = Settings()