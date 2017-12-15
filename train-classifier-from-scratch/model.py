import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import data_processing

data = data_processing.load_data(download=True)
new_data = data_processing.convert2onehot(data)


# prepare training data
new_data = new_data.values.astype(np.float32)   # change to numpy array and float32
np.random.shuffle(new_data)
sep = int(0.7 * len(new_data))
train_data = new_data[:sep] # training data (70%)
test_data = new_data[sep:]  # test data (30%)

# build network
tf_input = tf.placeholder(tf.float32, [None, 25], 'input')
tfx = tf_input[:, :21]
tfy = tf_input[:, 21:]

l1 = tf.layers.dense(tfx, 128, tf.nn.relu, name='l1')
l2 = tf.layers.dense(l1, 128, tf.nn.relu, name='l2')
out = tf.layers.dense(12, 4, name='l3')
prediction = tf.nn.softmax(out, name='pred')
