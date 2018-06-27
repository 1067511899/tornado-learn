import numpy as np
import matplotlib.pyplot as plot

num_points = 1000
vectors_set = []
# Create a few random data points
for i in range(num_points):
    W = 0.1  # W
    b = 0.4  # b
    x1 = np.random.normal(0.0, 1.0)
    nd = np.random.normal(0.0, 0.05)  # in:mean,standard deviation
    y1 = W * x1 + b
    y1 = y1 + nd
    vectors_set.append([x1, y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# plot.plot(x_data, y_data, 'ro', label='Originaldata')
# plot.legend()
# plot.show()

import tensorflow as tf
W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.6)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(6):
    sess.run(train)
    print(i, sess.run(W), sess.run(b), sess.run(loss))
    plot.plot(x_data, y_data, 'ro', label='Original data')
    plot.plot(x_data, sess.run(W) * x_data + sess.run(b))
    plot.xlabel('X')
    plot.xlim(-2, 2)
    plot.ylim(0.1, 0.6)
    plot.ylabel('Y')
    plot.legend()
    plot.show()
