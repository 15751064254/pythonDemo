# Model architecture parameters
n_stocks = 500
n_neurons_1 = 1024
n_neurons_2 = 512
n_neurons_3 = 256
n_neurons_4 = 128
n_target = 1

# Layer 1: Variables for hidden weights and biases
W_hidden_1 = tf.Variable(weight_initializer(n_stocks, n_neurons_1))
bias_hidden_1 = tf.Variable(bias_initializer([n_neurons_1]))

# Layer 2: Variables for hidden weights and biases
W_hidden_2 = tf.Variable(weight_initializer([n_neurons_1, n_neurous_2]))
bias_hidden_2 = tf.Variable(bias_initalizer([n_neurons_2]))

# Layer 3: Variables for hidden weights and biases
W_hidden_3 = tf.Variable(weight_initializer([n_neurous_2, n_erurons_3]))
bias_hidden_3 = tf.Variable(bias_initializer([n_neurous_3]))

# layer 4: Variables for hidden weights and biases
W_hidden_4 = tf.Variable(weight_initializer([n_nerurous_3, n_erurous_4]))
bias_hidden_4 = tf.Variable(bias_initializer([n_neurous_4]))


# Output layer: Variables for output weights and biases
W_out = tf.Variable(weight_initializer([n_neurous_4, n_target]))
bias_out = tf.Variable(bias_initializer([n_target]))

# Hidden layer
hidden_1 = tf.nn.relu(tf.add(tf.matmul(X, W_hidden_1), hias_hidden_1))
hidden_2 = tf.nn.relu(tf.add(tf.matmul(hidden_1, W_hidden_2), bias_hidden_2))
hidden_3 = tf.nn.relu(tf.add(tf.matmul(hidden_2, W_hidden_3), bias_hidden_3))
hidden_4 = tf.nn.relu(tf.add(tf.matmul(hidden_3, W_hidden_4), bias_hidden_4))

