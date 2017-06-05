from tensorflow.examples.tutorials.mnist import input_data
#this is a dataset of numbers between zero and nine that is squashed down into a vector of
#size 1x784
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#import tensorflow
import tensorflow as tf

#this should create a symbolic vector input for the data set
x = tf.placeholder(tf.float32, [None, 784])
