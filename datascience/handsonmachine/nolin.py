import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 生成随机变量
x_data = np.linspace(-1, 1, 200)  # 生成200个随机点，范围为-1 --> 1
x_data = x_data.reshape((200, 1))  # 维度设置为(200, 1)
noise = np.random.normal(0, 0.02, x_data.shape)  # 生成干扰项

y_data = np.square(x_data) + noise

x = tf.placeholder(tf.float32, [200, 1])
y = tf.placeholder(tf.float32, [200, 1])

# 定义神经网络中间层权值
weights_l1 = tf.Variable(tf.random_normal([1, 10]))  # 10个神经元
biases_l1 = tf.Variable(tf.zeros([1, 10]))
wx_plust_b_l1 = tf.matmul(x, weights_l1) + biases_l1
l1 = tf.nn.tanh(wx_plust_b_l1)  # 双曲正切函数作为激活函数

# 定义输出层
weights_l2 = tf.Variable(tf.random_normal([10, 1]))  # 输出层1个神经元
biases_l2 = tf.Variable(tf.zeros([1, 1]))  # 一个偏置
wx_plust_b_l2 = tf.matmul(l1, weights_l2) + biases_l2
prediction = tf.nn.tanh(wx_plust_b_l2)  # 预测结果

# 代价函数
loss = tf.reduce_mean(tf.square(y - prediction))
# 使用梯度下降
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 学习率设置为0.1

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 变量初始化，一定要做
    for _ in range(20000):
        sess.run(train_step, feed_dict={x:x_data, y:y_data})  # 使用梯度下降法进行训练参数

    # 获得预测值
    prediction_value = sess.run(prediction, feed_dict={x: x_data})  # 得到预测结果
    print(prediction_value)
    # 画图
    plt.figure()
    plt.scatter(x_data, y_data)  # 画散点图
    plt.plot(x_data, prediction_value, 'r-', lw=5)  # 画预测的实线，红色
    plt.show()

