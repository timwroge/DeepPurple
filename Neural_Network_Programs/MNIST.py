from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import math
from math import exp
from tensorflow.examples.tutorials.mnist import input_data

#import tensorflow
import tensorflow as tf

FLAGS = None

#this is a dataset of numbers between zero and nine that is squashed down into a vector of
#size 1x784

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#this should create a symbolic vector input for the data set
x = tf.placeholder(tf.float32, [None, 784])
#None means the dimension can be any length

#this will create the weights and biases for the model

#name_scope will provide visualizing capabilities for the data
#number of neurons per layer
K=200
L=100
M=60
N=30


#W and b are tensors full of zeros
#adding layers
W1= tf.Variable(tf.truncated_normal([784, K], stddev=0.1))
b1 = tf.Variable(tf.zeros([K]))
W2= tf.Variable(tf.truncated_normal([K, L],stddev=0.1))
b2 = tf.Variable(tf.zeros([L]))
W3= tf.Variable(tf.truncated_normal([L, M],stddev=0.1))
b3 = tf.Variable(tf.zeros([M]))
W4= tf.Variable(tf.truncated_normal([M, N],stddev=0.1))
b4 = tf.Variable(tf.zeros([N]))
W5= tf.Variable(tf.truncated_normal([N, 10],stddev=0.1))
b5 = tf.Variable(tf.zeros([10]))


#implementing multilayer nn
y1 = tf.nn.relu(tf.matmul(x, W1) + b1)
y2 = tf.nn.relu(tf.matmul(y1, W2) + b2)
y3 = tf.nn.relu(tf.matmul(y2, W3) + b3)
y4 = tf.nn.relu(tf.matmul(y3, W4) + b4)
y = tf.nn.softmax(tf.matmul(y4, W5) + b5) #matmul means matrix multiply

#define the cost function (loss)to be minimized, in this case it is the cross_entropy
#this is a placeholder  to input the correct answers
y_ = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
##multiply each element of y_ with the corresponding element of tf.log(y).
##Then tf.reduce_sum adds the elements in the second dimension of y, due to the reduction_indices=[1] parameter.
##Finally, tf.reduce_mean computes the mean over all the examples in the batch.
train_step = tf.train.GradientDescentOptimizer(.05).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
c=4.75*10**-4
epochs = 1000
for i in range(epochs):
  #training_rate=0.03*exp(-c*i)
  
    #by using small batches of a 100 data points as below, this utilizes stochastic gradient descent
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})



 # Test trained model on dataset
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy of trained model: ',sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))
