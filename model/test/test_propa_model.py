import pickle
import numpy as np
import pandas as pd

# load model
model = pickle.load(open('../svm_digit_recognizer_proba.pkl', 'rb'))

# load data
labeled_images = pd.read_csv('../data/train.csv')
images = labeled_images.iloc[:, 1:]
labels = labeled_images.iloc[:, :1]

idx = 3
test_image = images.iloc[idx, :].to_numpy().reshape((1, 784))
test_label = labels.iloc[idx, 0]
print(test_image)
print(f'expected value : {test_label}')
result_pro = model.predict_proba(test_image)
percentage = np.vectorize(lambda x: x*100)
percent_result = percentage(result_pro[0])
print(f'predicted value : {percent_result.argmax()} -> confident : {percent_result[percent_result.argmax()]:.2f}%')

for i, percent in enumerate(percent_result):
    print(f'{i} : {percent_result[i]:.2f}%')