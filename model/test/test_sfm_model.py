import pandas as pd
import numpy as np
import tensorflow as tf

def rescale_table(table) :
    table = table.astype("float32")
    for i in table :
        reshape_array = np.array(table[i]).reshape(-1,1)
        table[i] = reshape_array / 255.
    return table

training = pd.read_csv("../data/train.csv")

X_train = training.drop("label", axis=1)
y_train = training["label"]

X_train = rescale_table(X_train)

tf.compat.v1.disable_eager_execution()

init = tf.compat.v1.global_variables_initializer()

idx = 0

x = tf.compat.v1.placeholder(tf.float32, [None, 784], name='x')
W = tf.Variable(tf.zeros([784, 10]), name='W')
bias = tf.Variable(tf.zeros([10]), name='bias')
y_prediction = tf.nn.softmax(tf.matmul(x, W) + bias, name='y_prediction')

with tf.compat.v1.Session() as sess:
    new_saver = tf.compat.v1.train.import_meta_graph('../sfm/sfm_model.meta')
    new_saver.restore(sess, tf.train.latest_checkpoint('../sfm'))
    all_vars = tf.compat.v1.get_collection('vars')

    sess.run(init)

    predictions = y_prediction
    predicted_labels = predictions.eval(feed_dict={x: X_train.iloc[idx].to_numpy().reshape(1, 784)})
    print(predicted_labels, 'true label =', y_train.iloc[idx])