from fastapi import FastAPI
from src.service.model_manager import ModelManager
from typing import Callable, List


def _startup_model(app: FastAPI, model_path: str, tokenizer_name: str) -> None:
    model_manager = ModelManager()
    # use loop
    model_manager.add_model(model_path, tokenizer_name)
    app.state.model_manager = model_manager

def _shutdown_model(app: FastAPI) -> None:
    app.state.model_manager = None

def start_app_handler(app: FastAPI, model_paths: List[str], tokenizer_names: List[str]) -> Callable:
    def startup() -> None:
        model_manager = ModelManager()
        for model_path, tokenizer_name in zip(model_paths, tokenizer_names):
            model_manager.add_model(model_path, tokenizer_name)
        app.state.model_manager = model_manager

    return startup
    
def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)

    return shutdown