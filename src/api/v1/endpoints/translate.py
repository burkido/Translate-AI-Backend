from fastapi import APIRouter, Request
from typing import Any
from src.models.translate import TranslateRequest, TranslateResponse

router = APIRouter()

@router.post("/", response_model=TranslateResponse)
async def translate(request: Request, payload: TranslateRequest) -> TranslateResponse:
    source_lang = payload.source_lang
    target_lang = payload.target_lang
    text = payload.text

    model_manager = request.app.state.model_manager
    translated = model_manager.predict(
        model_name="/code/src/ml_model/opus-mt-mul-en.pkl",
        data=text
    )
    return TranslateResponse(translated_text=translated)