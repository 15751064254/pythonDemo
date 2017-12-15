from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


# pylint: disable=missing-docstring
import argparse
import os
import sys
import time

from six.moves import xrange    # pylint: disable=redefined-builtin
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.examples.tutorials.mnist import mnist

# Basic model parameters as external flags:
FLAGS = None

def placeholder_inputs(batch_size):
    """ Generate placeholder variables to represent the input tensors.
    These placeholders are used as inputs by the rest of the model building
    code and will be fed from the downloaded data in the .run() loop, below.


    Args:
        batch_size: The batch size will be baked into both placeholders.

    Return:
        images_placeholder: Images placeholder.
        labels_placeholder: Lables placeholder.
    """

    # Note that the shapes fo the placeholders mathc the shapes of the full
    # image and lable tensors, except the first dimension is now batch_size
    # rather than the full size fo the train or test data sets.
    images_placeholder = tf.placeholder(tf.float32, shape=(batch_size, mnist.IMAGE_PIXELS))
    lables_placeholder = tf.placeholder(tf.float32, shape=(batch_size)))
    return images_placeholder, labels_placeholder

def fill_feed_dict(data_set, images_pl, lables_pl):
    """ Fills the feed_dict for training the given step.

    A feed_dict takes the form of:
    feed_dict = {
        <placeholder>: <tensor fo values to be passed for placeholder>,
        ...
    }


    Args:
        data_set: The set of images and lables, from input_data.read_data_sets()
        images_pl: The images placeholder, from placeholder_inputs().
        labels_pl: The lables placeholder, from placeholder_inputs().

    Returns:
        feed_dict: The feed dictionary mapping from placeholders to values.
    """

    # Create the feed_dict for the placeholders filled with the next
    # 'batch size' examples.
    images_feed, lables_feed = data_set.next_batch(FLAGS.batch_size, FLAGS.fake_data)

    feed_dict = {
            images_pl: images_feed,
            labels_pl: labels_feed,
    }

    return feed_dict


def do_eval(sess,
            eval_correct,
            images_placeholder,
            labels_placeholder,
            data_set):





























