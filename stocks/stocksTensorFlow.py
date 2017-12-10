import tensorflow as tf

# Define a and b as placeholders
a = tf.placeholder(dtype=tf.int8)
b = tf.placeholder(dtype=tf.int8)

# Define the addition
c = tf.add(a, b)

# Initialize the graph
session = tf.Session()

# Run the graph
session.run(c, feed_dict={a: 5, b: 4})
