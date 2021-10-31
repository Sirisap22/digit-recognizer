import numpy as np
import pandas as pd
import tensorflow as tf

training = pd.read_csv("data/train.csv")

def rescale_table(table) :
    table = table.astype("float32")
    for i in table :
        reshape_array = np.array(table[i]).reshape(-1,1)
        table[i] = reshape_array / 255.
    return table

def one_hot_encode(series) :
    return pd.get_dummies(series).values

X_train = training.drop("label", axis=1)
y_train = training["label"]

X_train = rescale_table(X_train)
y_train = one_hot_encode(y_train)

learning_rate = 0.3
epochs = 100

tf.compat.v1.disable_eager_execution()
x = tf.compat.v1.placeholder(tf.float32, [None, 784], name='x')
W = tf.Variable(tf.zeros([784, 10]), name='W')
bias = tf.Variable(tf.zeros([10]), name='bias')
tf.compat.v1.add_to_collection('vars', x)
tf.compat.v1.add_to_collection('vars', W)
tf.compat.v1.add_to_collection('vars', bias)

y_true = tf.compat.v1.placeholder(tf.float32, [None, 10], name='y_true')
y_prediction = tf.nn.softmax(tf.matmul(x, W) + bias, name='y_prediction')
tf.compat.v1.add_to_collection('vars', y_prediction)

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_prediction, labels=y_true))

correct_predictions = tf.equal(tf.argmax(y_prediction,1), tf.argmax(y_true,1))
accuracy_measure = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

training_step = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

saver = tf.compat.v1.train.Saver()
sess = tf.compat.v1.InteractiveSession()

init = tf.compat.v1.global_variables_initializer()
sess.run(init)

for i in range(epochs + 1):
    sess.run(training_step, feed_dict={x: X_train, y_true: y_train})
    print("Epoch " + str(i) + " accuracy: " + str(sess.run(accuracy_measure, feed_dict={x: X_train, y_true: y_train})))

saver.save(sess, 'sfm_model')
sess.close()