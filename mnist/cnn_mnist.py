""" Convolutional Neural Network Estimator for MNIST, built with tf.layers. """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

def cnn_model_fu(features, labels, mode):
    """ Model function for CNN. """

    # Input Layer
    # Reshape X to 4-D tensor: [batch_size, width, height, channels]
    # MNIST images are 28x28 pixels, and have one color channel
    input_layer = tf.reshape(features['x'], [-1, 28, 28, 1])

    Convolutional Layer #1
