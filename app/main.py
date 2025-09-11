from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import predict

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

@app.get("/hello_miss")
def say_hello(name: str = "Miss beautifull"):
    return {"message": f"Hello {name}!"} 	  

@app.get("/Salam")
def say_hello(name: str = "la vie est belle"):
    return {"message": f"Hey {name}!"}
