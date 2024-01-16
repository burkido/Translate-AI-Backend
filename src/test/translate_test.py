import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from pydantic import BaseModel
from src.main import app, translate

class TranslateRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

class TranslateResponse(BaseModel):
    translated_text: str

client = TestClient(app)

@patch('main.model_manager')
def test_translate(mock_model_manager):
    mock_request = Mock()
    mock_request.app.state.model_manager = mock_model_manager

    test_cases = [
        (TranslateRequest(source_lang="it", target_lang="en", text="Come stai?"), ["How are you?"]),
        (TranslateRequest(source_lang="en", target_lang="it", text="How are you?"), ["Come stai?"]),
        (TranslateRequest(source_lang="it", target_lang="de", text="Come stai?"), ["Wie geht es dir?"])
    ]

    for req, expected in test_cases:
        mock_model_manager.predict.return_value = expected
        response = translate(mock_request, req)
        assert response.translated_text == expected