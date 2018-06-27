from tensorflow.examples.tutorials.mnist import input_data
 
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# 
# print(mnist.train.images.shape)
# print(mnist.train.images[0, :])
# 
# import scipy.misc
# import os
# save_dir = 'MNIST_data/raw/'
# if os.path.exists(save_dir) is False:
#     os.makedirs(save_dir)
# 
# for i in range(20):
#     image_array = mnist.train.images[i, :]
#     image_array = image_array.reshape(28, 28)
#     filename = save_dir + 'mnist_train_%d.jpg' % i
#     scipy.misc.toimage(image_array, cmin=0.0 , cmax=1.0).save(filename)
#     

import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y)))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x:mnist.test.images, y_:mnist.test.labels}))
