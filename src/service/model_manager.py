import pickle
from transformers import AutoTokenizer
import os

class ModelManager:
    def __init__(self):
        self.models = {}
    
    def add_model(self, model_path, tokenizer_name):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        model_name = os.path.basename(model_path)
        self.models[model_name] = {'model': model, 'tokenizer': tokenizer}
    
    def remove_model(self, model_name):
        del self.models[model_name]

    def predict(self, model_name, data):
        model = self.models[os.path.basename(model_name)]['model']
        tokenizer = self.models[os.path.basename(model_name)]['tokenizer']
        input_ids = tokenizer(data, return_tensors='pt').input_ids
        outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=1)
        result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return result