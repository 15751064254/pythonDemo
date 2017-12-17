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
    """ Runs one evaluation against the full epoch of data.

    Args:
        sess: The session in which the model has been trained.
        eval_correct: The Tensor that returns the number of correct predictions.
        images_placeholder: The image placeholder.
        labels_placeholder: The labels placeholder.
        data_set: The set of images and labels to evaluate, form imput_data.read_data_sets().
    """
    # And run one epoch of eval.
    true_count = 0  # Counts the number of correct predictions.
    steps_pre_epoch = data_set.num_examples     // FLAGS.batch_szie
    num_examples = steps_pre_epoch * FLAGS.batch_size
    for step in xrange(steps_per_epoch):
        feed_dict = fill_feed_dict(data_set,
                                    images_placeholder,
                                    labels_placeholder)
        true_count += sess.run(eval_correct, feed_dict=feed_dict)
    precision = float(true_count) / num_examples
    print(' Num examples: %d Num correct: %d Precision @ 1: %0.04f' % 
            num_examples, true_count, precision)


def run_training():
    """ Train MNIST for a number of steps."""
    # Get the sets of images and labels for training, validation, and
    # test on MNIST.
    data_sets =  input_data.read_data_sets(FLAGS.input_data_dir, FLAGS.fake_data)
    # Tell TensorFlow that the model will be built into the default Graph.
    with tf.Graph().as_default():
        # Generate placeholders for the images and labels.
        images_placeholder, labels_placeholder = placeholder_inputs(
            FLAGS.batch_size)
        # Build a Graph that computes predictions from the inference model.
        logits = mnist.inference(images_placeholder,
                                    FLAGS.hidden1,
                                    FLAGS.hidden2)
        # Add to the Graph the Ops for loss calculation.
        loss = mnist.loss(logits, labels_placeholder)

        # Add the Op to comper the logits to the labels during evaluation.
        eval_correct = mnist.evaluation(logits, labels_placeholder)

        # Build the summary Tensor based on the TF collection of Summaries.
        summary = tf.summary.merge_all()

        # Add the variable initializer Op.
        init = tf.global_variables_initializer()

        # Create a save for writing training checkpoints.
        saver = tf.train.Saver()

        # Create a session for running Ops on the Graph.
        sess = tf.Session()

        # Instantiate a SummaryWriter to output summaries and the Graph.
        summary_writer = tf.summary.FileWriter(FLAGS.log_dir, sess.graph)

        # Run the Op to initialize the variable.
        sess.run(init)

        # Start the training loop.
        for step in xrange(FLAGS.max_steps):
            start_time = time.time()

            # Fill 





























