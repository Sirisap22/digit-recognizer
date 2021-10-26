import pickle
import numpy as np
import pandas as pd



def test_train_set(model):
    # load data
    labeled_images = pd.read_csv('../data/train.csv')
    images = labeled_images.iloc[:, 1:]
    labels = labeled_images.iloc[:, :1]

    idx = 3
    test_image = images.iloc[idx, :].to_numpy().reshape((1, 784)) / 255.
    test_label = labels.iloc[idx, 0]
    print(test_image)
    print(f'expected value : {test_label}')
    result_pro = model.predict_proba(test_image)
    percentage = np.vectorize(lambda x: x*100)
    percent_result = percentage(result_pro[0])
    print(f'predicted value : {percent_result.argmax()} -> confident : {percent_result[percent_result.argmax()]:.2f}%')

    for i, percent in enumerate(percent_result):
        print(f'{i} : {percent:.2f}%')

def test_test_set(model):
    test_data = pd.read_csv('../data/test.csv')
    results = model.predict(test_data) / 255.

    df = pd.DataFrame(results)
    df.index.name='ImageId'
    df.index+=1
    df.columns=['Label']

    df.to_csv('results_not.csv', header=True)

    # not normalize 0.97360 No. 939th
    # normalize 0.97360 - No. 939th
    # full normalize 0.97521 - No.901st

if __name__ == '__main__':
    # load model
    model = pickle.load(open('../svm_digit_recognizer_proba_normalize_full.pkl', 'rb'))
    test_test_set(model)