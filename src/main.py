from fastapi import FastAPI

from src.core.config import settings
from src.api.v1.api import api_router

from src.core.event_handler import start_app_handler, stop_app_handler

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

app.add_event_handler("startup", start_app_handler(
    app,
    [
        "/code/src/ml_model/en-ar/model-opus-mt.pkl",
        "/code/src/ml_model/en-az/model-opus-mt.pkl",
        "/code/src/ml_model/en-de/model-opus-mt.pkl",
        "/code/src/ml_model/en-es/model-opus-mt.pkl",
        "/code/src/ml_model/en-fr/model-opus-mt.pkl",
        "/code/src/ml_model/en-hi/model-opus-mt.pkl",
        "/code/src/ml_model/en-it/model-opus-mt.pkl",
        "/code/src/ml_model/en-ru/model-opus-mt.pkl",
        "/code/src/ml_model/en-tr/model-opus-mt.pkl",
        "/code/src/ml_model/en-zh/model-opus-mt.pkl",
        "/code/src/ml_model/mul-en/model-opus-mt.pkl",
     ],
    [
        "Helsinki-NLP/opus-mt-en-ar",
        "Helsinki-NLP/opus-mt-en-az",
        "Helsinki-NLP/opus-mt-en-de",
        "Helsinki-NLP/opus-mt-en-es",
        "Helsinki-NLP/opus-mt-en-fr",
        "Helsinki-NLP/opus-mt-en-hi",
        "Helsinki-NLP/opus-mt-en-it",
        "Helsinki-NLP/opus-mt-en-ru",
        "Helsinki-NLP/opus-tatoeba-en-tr",
        "Helsinki-NLP/opus-mt-en-zh",
        "Helsinki-NLP/opus-mt-mul-en",
    ]
    ))

app.add_event_handler("shutdown", stop_app_handler(app))


@app.get("/")
def root():
    return {"message": "Hello World"}