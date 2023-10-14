from pydantic import BaseModel
from typing import List

class TranslateRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

class TranslateResponse(BaseModel):
    translated_text: List[str]