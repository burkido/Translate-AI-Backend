from fastapi import FastAPI

def _startup_model(app: FastAPI, model_path: str) -> bool:
    opust_mt_mul_en = MLModel(model_path)
    app.state.opust_mt_mul_en = opust_mt_mul_en