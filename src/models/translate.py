from pydantic import BaseModel

class TranslateRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

class TranslateResponse(BaseModel):
    translated_text: str