from fastapi import UploadFile
from PIL import Image
import numpy as np
import tensorflow as tf

def predict_sfm(file: UploadFile):
    im = np.array(Image.open(file.file).convert('L').resize((28, 28)))
    image = im.flatten().reshape((1,784))

    # normalize
    image = image / 255.

    tf.compat.v1.disable_eager_execution()
    init = tf.compat.v1.global_variables_initializer()

    x = tf.compat.v1.placeholder(tf.float32, [None, 784], name='x')
    W = tf.Variable(tf.zeros([784, 10]), name='W')
    bias = tf.Variable(tf.zeros([10]), name='bias')
    y_prediction = tf.nn.softmax(tf.matmul(x, W) + bias, name='y_prediction')

    with tf.compat.v1.Session() as sess:
        

        # load model
        new_saver = tf.compat.v1.train.import_meta_graph('../model/sfm/sfm_model.meta')
        new_saver.restore(sess, tf.train.latest_checkpoint('../model/sfm'))
        all_vars = tf.compat.v1.get_collection('vars')

        sess.run(init)

        predictions = y_prediction
        predicted_labels = predictions.eval(feed_dict={x: image})[0]
    
    tf.compat.v1.reset_default_graph()

    prediction = {}
    for i, _ in enumerate(predicted_labels):
        prediction[i] = f'{predicted_labels[i] * 100:.2f}'


    return prediction