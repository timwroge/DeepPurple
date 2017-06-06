####################################
####################################
##############WARNING###############
####################################
###THIS PROGRAM TOOK MY COMPUTER####
##########LIKE AN HOUR TO RUN#######
#########SO KEEP THAT IN MIND#######
####################################
####################################


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

#import tensorflow
import tensorflow as tf
sess = tf.InteractiveSession()
FLAGS = None

#this is a dataset of numbers between zero and nine that is squashed down into a vector of
#size 1x784
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#here are the default functions that will allow the computation to be easier

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

#this will now provide some convolution underpinnings to make more computation easier going forward

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
###########################
####### CONVOLUTION #######
###########################
#for the first convolutional layer......
#this will first start with convolution, followed by max pooling
#the dimensions are listed in the order: [patchsizedim1,patchsizedim2,number of input channels, number of output channels]

W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
#we now reshape x into a 4d tensor, with the second and third dimensions corresponding to image width and height and the final
#corresponding to the number of color channels
x_image = tf.reshape(x, [-1,28,28,1])
#this image will then be convoluted using the weight tensor and then adding the bias
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

#Second convolutional layer
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

#this part is the "densely connected layer as named by tensorflow.com
#this will add a fully connencted layer with 1024 neurons to process the whole image

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

#now we apply a dropout to prevent overfitting  before the readout layer
#there is a placeholder for the probability that the neuron's output is kept during dropout 
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#we will now have the readout layer (soft max regression
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

###########################
#### TRAINING PHASE #######
###########################
#differences between this and the simple single layer NN include using the ADAM optimizer, and adding logging for every 100th iteration


cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.global_variables_initializer())
for i in range(20000):
  batch = mnist.train.next_batch(50)
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
###########################
####### ACCURACY ##########
###########################

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))





