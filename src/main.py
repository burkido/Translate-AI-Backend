from fastapi import FastAPI
import pickle
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from src.core.config import settings

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-mul-en")

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(healthcheck_router)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/translate")
def translateFromMultToEn(input):
    print(input)
    print(type(tokenizer))
    model = pickle.load(open('src/ml_model/opus-mt-mul-en/model-opus-mt-mul-en.pkl', 'rb'))

    input_ids = tokenizer(input, return_tensors='pt').input_ids
    outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=1)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)