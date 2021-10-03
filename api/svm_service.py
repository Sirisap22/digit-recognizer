from fastapi import UploadFile
from PIL import Image
import pickle
import numpy as np

def predict(file: UploadFile):
    im = np.array(Image.open(file.file).convert('L').resize((28, 28)))
    image = im.flatten().reshape((1,784))
    # load model
    model = pickle.load(open('../model/svm_digit_recognizer_proba.pkl', 'rb'))

    result_pro = model.predict_proba(image)
    percentage = np.vectorize(lambda x: x*100)
    percent_result = percentage(result_pro[0])

    prediction = {}
    for i, _ in enumerate(percent_result):
        prediction[i] = f'{percent_result[i]:.2f}'

    return prediction