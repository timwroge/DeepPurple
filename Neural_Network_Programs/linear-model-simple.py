# This is copied from the tensorflow startup tutorial, just to validate that it is working 
# and to get a comprehensive idea of how to go about setting up a network with tensorflow
import tensorflow as tf
import numpy as np
# NumPy is often used to load/preprocess data

# List of features -- ? 
features = [tf.contrib.layers.real_valued_column("x",dimension=1)]

# An estimator is the front end to invoking training and evaluaton
# Many predefined types like linear, logistic, and other regression and
# classification estimators 
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

# tensorflow provides many helper methods to read and set up data sets 
# numpy_input_fn is a good example 
# num_epochs= how many batches 
x = np.array([1.,2.,3.,4.])
y = np.array([0.,-1.,-2.,-3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x},y,batch_size=4,
        num_epochs=1000)

# here we invoke 1000 training steps 
estimator.fit(input_fn=input_fn,steps=1000)

# now to evaluate how well the model did 

print(estimator.evaluate(input_fn=input_fn))

# to create a custom model, we can use lower level code from the other
# example 

def model(features,labels,mode):
    W = tf.get_variable("W",[1],dtype=tf.float64)
    b = tf.get_variable("b",[1],dtype=tf.float64)
    y = W*features['x']+b
    loss = tf.reduce_sum(tf.square(y-labels))

    global_step = tf.train.get_global_step()
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = tf.group(optimizer.minimize(loss),tf.assign_add(global_step,1))

    return tf.contrib.learn.ModelFnOps(mode=mode, predictions=y,loss=loss,
            train_op=train)

estimator = tf.contrib.learn.Estimator(model_fn=model)
x = np.array([1.,2.,3.,4.])
y = np.array([0.,-1.,-2.,-3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x},y,4,num_epochs=1000)
estimator.fit(input_fn=input_fn, steps=1000)
print(estimator.evaluate(input_fn=input_fn,steps=10))

