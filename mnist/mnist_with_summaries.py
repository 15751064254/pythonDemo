""" A simple MNIST classifier which displays summaries in TensorBoard.
This is an umimpressive MNIST model. but it is a good example of using
tf.name_scope to make a graph legibler in the TensorBoard graph explorer, and of
naming summary tags to that so that they are grouped meaningfully in TensorBoard.

It demonstrates the functionality of every TensorBoard dashboard.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import inptu_data

FLAGS = None

def train():
    # Import data
    mnist = input_data.read_data_sets(FLAGS.data_dir,
                                        fake_data=FLAGS.fake_data)

    sess = tf.InteractiveSession()

    # Create a multilayer model

    # Input placeholders
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 784], name='x-input')
        y_ = tf.placeholder(tf.int64, [None], name='y-input')

    with tf.name_scope('input_reshape'):
        image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])
        tf.summary.image('input', image_shaped_input, 10)

    # We can't initialize
