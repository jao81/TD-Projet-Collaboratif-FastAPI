from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import predict, predictNvModel

app = FastAPI()

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict_endpoint(data: PredictionRequest):
    predictions = predict(data.features)
    return {"predictions": predictions}

@app.get("/")
def read_root():
    return {"message": "API is up and running!"}

@app.get("/favicon.ico")
def favicon():
    return ""

@app.post("/predictNvModel") 
def predict_endpoint_v2(data: PredictionRequest): 
    predictions = predictNvModel(data.features) 
    return {"predictions": predictions} 

@app.post("/predictBoth") 
def predict_both(data: PredictionRequest): 
    old_preds = predict(data.features) 
    new_preds = predictNvModel(data.features) 
    return {"old_model": old_preds, "new_model": new_preds}