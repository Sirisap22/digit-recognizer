import numpy as np
import pandas as pd
import tensorflow as tf

from matplotlib import pyplot as plt
import seaborn as sns
#%matplotlib inline
sns.set_style("whitegrid")

import warnings
warnings.filterwarnings("ignore")

training = pd.read_csv("../data/train.csv")
testing = pd.read_csv("../data/test.csv")

training.head()
#print(training.shape)

X_train = training.drop("label", axis=1)
y_train = training["label"]
ax = plt.hist(y_train)

plt.figure(figsize=(14, 10))

def show_images(numbers):
    for i in range(1, numbers + 1):
        plt.subplot(5, 10, i)
        plt.imshow(X_train.iloc[i].values.reshape(28,28),cmap='gray')
        plt.xticks([]), plt.yticks([])
        plt.title(y_train[i])

show_images(50)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

def rescale_table(table) :
    table = table.astype("float32")
    for i in table :
        reshape_array = np.array(table[i]).reshape(-1,1)
        table[i] = scaler.fit_transform(reshape_array)
    return table

X_train = rescale_table(X_train)

X_test = testing
X_test = rescale_table(X_test)

#print(X_train.sample(10))

####reduce space#######
del training 
del testing 

#print(set(y_train)) num0-9in y-axis

def one_hot_encode(series) :
    return pd.get_dummies(series).values

y_train = one_hot_encode(y_train)

from sklearn.model_selection import train_test_split

X_training, X_valid, y_training, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=0)

learning_rate = 0.3
epochs = 100

tf.compat.v1.disable_eager_execution()
x = tf.compat.v1.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
bias = tf.Variable(tf.zeros([10]))

y_true = tf.compat.v1.placeholder(tf.float32, [None, 10])
y_prediction = tf.nn.softmax(tf.matmul(x, W) + bias)

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_prediction, labels=y_true))

correct_predictions = tf.equal(tf.argmax(y_prediction,1), tf.argmax(y_true,1))
accuracy_measure = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

training_step = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

sess = tf.compat.v1.InteractiveSession()

init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for i in range(epochs + 1):
    sess.run(training_step, feed_dict={x: X_train, y_true: y_train})
    print("Epoch " + str(i) + " accuracy: " + str(sess.run(accuracy_measure, feed_dict={x: X_valid, y_true: y_valid})))

sess.run(accuracy_measure, feed_dict={x: X_valid, y_true: y_valid})

predictions = tf.argmax(y_prediction, 1)
predicted_labels = predictions.eval(feed_dict={x: X_test})
print(predictions.eval(feed_dict={x: X_test}))
sess.close()