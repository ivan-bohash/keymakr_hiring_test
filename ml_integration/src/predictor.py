import joblib
import os

class PriorityPredictor:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            return None
        return joblib.load(self.model_path)

    def predict(self, text: str) -> str:
        if self.model is None:
            # try again to load model
            self.model = self.load_model()
            if self.model is None:
                return "Model not initialized"
        
        return self.model.predict([text])[0]