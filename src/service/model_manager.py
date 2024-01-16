import pickle
from transformers import AutoTokenizer
import os

class ModelManager:
    def __init__(self):
        self.models = {}
    
    def add_model(self, model_path, tokenizer_name):
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.models[model_path] = {'model_path': model_path, 'tokenizer': tokenizer}
    
    def remove_model(self, model_name):
        del self.models[model_name]

    def predict(self, model_name, data):
        with open(self.models[model_name]['model_path'], 'rb') as f:
            model = pickle.load(f)
        
        tokenizer = self.models[model_name]['tokenizer']
        input_ids = tokenizer(data, return_tensors='pt').input_ids

        outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=1)
        result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return result