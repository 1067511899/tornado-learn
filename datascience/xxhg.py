import tensorflow as tf
import numpy as np

trX = np.linspace(-1, 1, 101)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.4 + 0.2

import matplotlib.pyplot as plt

plt.scatter(trX, trY)
plt.plot(trX, .2 + 2 * trX)
X = tf.placeholder("float", name="X")
Y = tf.placeholder("float", name="Y")
with tf.name_scope("Model"):

    def model(X, w, b):
        return tf.multiply(X, w) + b
    
    w = tf.Variable(-1.0, name="b0")
    b = tf.Variable(-2.0, name="b1")
    y_model = model(X, w, b)
    
    with tf.name_scope("CostFunction"):
        cost = (tf.pow(Y - y_model, 2))
        train_op = tf.train.GradientDescentOptimizer(0.05).minize(cost)

#         cost_op = tf.scalar_summary
