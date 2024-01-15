import pickle
from transformers import AutoTokenizer
import os

class ModelManager:
    def __init__(self):
        self.models = {}
    
    def add_model(self, model_path, tokenizer_name):
        print("model_manager.py ALOOOOOOOOOOOOOO || model_path: ", model_path, "tokenizer_name: ", tokenizer_name)
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        print("All model names: ADD MODEL", self.models.keys())

        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.models[model_path] = {'model': model, 'tokenizer': tokenizer}
    
    def remove_model(self, model_name):
        del self.models[model_name]

    def predict(self, model_name, data):

        print("predict || All model names:", self.models.keys())

        print("predict || model_name", model_name, "path: ", os.path.basename(model_name))

        model = self.models[model_name]['model']
        tokenizer = self.models[model_name]['tokenizer']
        input_ids = tokenizer(data, return_tensors='pt').input_ids

        print("predict || tokenizer: ", tokenizer)

        outputs = model.generate(input_ids=input_ids, num_beams=5, num_return_sequences=1)
        result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return result