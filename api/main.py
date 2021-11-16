from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import svm_service
import sfm_service
import json
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
ORIGIN = os.getenv('ORIGIN')

app = FastAPI()
origins = [
    ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/model_v1/predict/svm')
async def predict(file: UploadFile = File(...)):
    prediction = svm_service.predict_svm(file)
    json_pred = json.dumps(prediction)
    return json_pred


@app.post('/model_v1/predict/sfm')
async def predict(file: UploadFile = File(...)):
    prediction = sfm_service.predict_sfm(file)
    json_pred = json.dumps(prediction)
    return json_pred

if __name__ == "__main__":
    uvicorn.run(app, host=f'{HOST}', port=int(PORT))