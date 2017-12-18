""" Simple MNISTclassifier example with JIT XLA and timelines. """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.client import timeline

FLAGS = None

def main(_):
    # Improt data
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    # Create the model
    x = tf.placeholder(tf.float32, [None, 784])
    w = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.matmul(x, w) + b

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 10])

    # The raw formulation of cross-entropy,

    # tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                              reduction_indices=[1]))
    can he numerically nustable.

    # So here we use tf.losses.sparse_softmax_cross_entropy on the raw
    # logit outputs of 'y', and the average across the batch.
    cross_entropy = tf.losses.spare_softmax_cross_entropy(labels=y_, logits=y)
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    config = tf.ConfigProto()
    jit_level = 0
    if FLAGS.xla:
        # Turns on XLA JIT compilation.
        jit_level = tf.OptimizerOptions.ON_1

    config.graph_options.optimizer_options.global_jit_level = jit_level
    run_metadata = tf.RunMetadata()
    sess = tf.Session(config=config)
    tf.global_variables_initializer().run(session=sess)

    # Train
    train_loops = 1000
    for i in range(train_loops):
        batch_xs, batch_ys = mnist.train.next_batch(100)

        # Create a timeline for the last loop and export to json to view with
        # chrome://tracing/.
        if  i == train_loops - 1:
            sess.run(
                train_step,
                feed_dict={
                    x: batch_xs,
                    y_: batch_ys
                },
                options=tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE),
                run_metadata=run_metadata
            )
            trace = timeline.Timeline(step_stats=run_metadata.step_stats)
            with open('timeline.ctf.json', w) as trace_file:
                trace_file.write(trace.generate_chrome_trace_format())

        else:
            sess.run(train_step, )
