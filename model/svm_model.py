import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn import svm

# load data
labeled_images = pd.read_csv('data/train.csv')
images = labeled_images.iloc[:, 1:]
labels = labeled_images.iloc[:,:1]

# normalize
images = images / 255.

# train model
model = svm.SVC(decision_function_shape='ovr', probability=True)

model.fit(images, labels.values.ravel())

# save model
print('saving model...')
pickle.dump(model, open('svm_digit_recognizer_proba_normalize_full.pkl', 'wb'))
print('saved')
