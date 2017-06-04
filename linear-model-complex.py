# This is copied from the tensorflow startup tutorial, just to validate that it is working 
# and to get a comprehensive idea of how to go about setting up a network with tensorflow
import numpy as np
import tensorflow as tf

# Model Parameters
W = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)
# Model input and output 
x = tf.placeholder(tf.float32)
linear_model = W*x+b
y = tf.placeholder(tf.float32)
# Loss function
loss = tf.reduce_sum(tf.square(linear_model-y)) # sum of the squares
# optimizer 
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset the values to the wrong ones
for i in range(1000):
    sess.run(train,{x:x_train,y:y_train})
# eval accuracy 
curr_w,curr_b,curr_loss = sess.run([W,b,loss],{x:x_train,y:y_train})
print("W: %s b: %s loss: %s"%(curr_w,curr_b,curr_loss))
