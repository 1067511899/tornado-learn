import tensorflow as tf

W = tf.Variable(tf.zeros([2, 1]), name='weights')

b = tf.Variable(0., name='bias')


def inference(X):
    return tf.matmul(X, W) + b


def loss(X, Y):
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))


def inputs():
    weight_age = [[84, 46], [73, 20], [62, 50], [70, 30],
                [76, 57], [69, 25], [72, 63], [79, 57], [75.44],
                [27, 24], [89, 31]]
    blood_fat_content = [354, 190, 405, 263, 451, 302, 288, 385, 402, 365, 290]
    return tf.to_float(blood_fat_content)


def train(total_loss):
    learning_rate = 0.0000001
    return 


tr.train.Gradie
