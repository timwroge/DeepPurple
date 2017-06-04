import tensorflow as tf
import numpy as np 
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# this program uses softmax regression, which provides probabilities of
# something being in a category 

# this sort of regression has two steps 
# first, add up evidence of being in a certain class 
# second, convert to probabilities 

x = tf.placeholder(tf.float32,[None,784]) # input for later, anything by 784 

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W)+b)

# many loss models out there, one good one is cross-entropy
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
# train the network
for _ in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print(sess.run(accuracy,feed_dict={x: mnist.test.images,
                                    y_:mnist.test.labels}))

