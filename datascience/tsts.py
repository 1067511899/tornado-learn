import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

data = pd.read_csv('train.csv')

# fill nan values with 0
data = data.fillna(0)
# convert ['male', 'female'] values of Sex to [1, 0]
data['Sex'] = data['Sex'].apply(lambda s: 1 if s == 'male' else 0)
# 'Survived' is the label of one class,
# add 'Deceased' as the other class
data['Deceased'] = data['Survived'].apply(lambda s: 1 - s)

# select features and labels for training
X = data[['Sex', 'Age', 'Pclass', 'SibSp', 'Parch', 'Fare']].as_matrix()
Y = data[['Deceased', 'Survived']].as_matrix()

batch_size = 8
w1 = tf.Variable(tf.random_normal([6, 2], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))

x = tf.placeholder(tf.float32, shape=(None, 6), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 2), name='y-input')

biases1 = 0.1
biases2 = 0.2

a = tf.nn.relu(tf.matmul(x, w1) + biases1)
y = tf.nn.relu(tf.matmul(a, w2) + biases2)

# a = tf.matmul(x, w1)
# y = tf.matmul(a, w2)

cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# rdm = RandomState(1)
# dataset_size = 2560
# X = rdm.rand(dataset_size, 2)
# Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    print(sess.run(w1))
    print(sess.run(w2))

    STEPS = 15000
    for i in range(STEPS):
        start = (i * batch_size) % 892
        end = min(start + batch_size, 892)
        
        sess.run(train_step, feed_dict={x:X[start:end], y_:Y[start:end]})
        if i % 1000 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x:X, y_:Y})
            print("After %d training step(s),cross entropy on all data is %g" % 
                  (i, total_cross_entropy))
    print(sess.run(w1))
    print(sess.run(w2))
