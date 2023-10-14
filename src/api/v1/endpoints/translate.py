from fastapi import APIRouter, Request

from src.models.translate import TranslateRequest, TranslateResponse

router = APIRouter()

@router.post("/translate", response_model=TranslateResponse)
async def translate(request: Request, payload: TranslateRequest) -> Any:
    source_lang = payload.source_lang
    target_lang = payload.target_lang
    text = payload.text

    translated_text = request.app