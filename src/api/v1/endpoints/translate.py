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

    if target_lang == 'en':
        model_path = "/code/src/ml_model/mul-en/model-opus-mt.pkl"
        translated = model_manager.predict(
            model_name=model_path,
            data=text
        )
        return TranslateResponse(translated_text=translated[0])
    elif source_lang == 'en':
        model_path = f"/code/src/ml_model/en-{target_lang}/model-opus-mt.pkl"
        translated = model_manager.predict(
            model_name=model_path,
            data=text
        )
        return TranslateResponse(translated_text=translated[0])
    else:
        model_path = f"/code/src/ml_model/mul-en/model-opus-mt.pkl"
        translated = model_manager.predict(
            model_name=model_path,
            data=text
        )
        model_path = f"/code/src/ml_model/en-{target_lang}/model-opus-mt.pkl"
        translated = model_manager.predict(
            model_name=model_path,
            data=translated
        )
        return TranslateResponse(translated_text=translated[0])