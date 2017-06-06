from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

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


#W and b are tensors full of zeros
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

#add summary operations for TENSORBOARD
w_h=tf.histogram_summary("weights", W)
b_h=tf.histogram_summary("weights", b)

#implementing the model with one line!
y = tf.nn.softmax(tf.matmul(x, W) + b) #matmul means matrix multiply

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
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

epochs = 30000
for _ in range(epochs):
    #by using small batches of a 100 data points as below, this utilizes stochastic gradient descent
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})



 # Test trained model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy of trained model: ',sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))
