from fastapi import APIRouter, Request
from typing import Any
from src.models.translate import TranslateRequest, TranslateResponse

router = APIRouter()

@router.post("/", response_model=TranslateResponse)
async def translate(request: Request, payload: TranslateRequest) -> TranslateResponse:
    print("translate.py || payload: ", payload)
    source_lang = payload.source_lang
    target_lang = payload.target_lang
    text = payload.text

    print("translate.py  || source_lang: ", source_lang, "target_lang: ", target_lang, "text: ", text)

    model_path = f"/code/src/ml_model/{source_lang}-{target_lang}/model-opus-mt.pkl"
    print("source_lang: ", source_lang, "target_lang: ", target_lang, "text: ", text, "model_path: ", model_path)

    model_manager = request.app.state.model_manager
    translated = model_manager.predict(
        model_name=model_path,
        data=text
    )

    return TranslateResponse(translated_text=translated)