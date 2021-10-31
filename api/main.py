from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import svm_service
import sfm_service
import json
import uvicorn

HOST = '127.0.0.1'
PORT = '8000'

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5000",
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