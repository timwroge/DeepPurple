import tensorflow as tf

node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0) # uses the tf.float32 implicitly! 
print(node1,node2)
#this is the output of the last command
##tensor("Const:0", shape=(), dtype=float32)
##tensor("Const_1:0", shape=(),dtype=float32)

#this will output the values of node1 and node 2 as they are defined

sess = tf.Session()
print(sess.run([node1,node2]))


node3 = tf.add(node1,node2)
print("node3: ",node3)
print("sess.run(node3): ",sess.run(node3))

# Placeholders are inputs to the graph
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # + does exactly what tf.add() does
# there's a feed dict parameter that are fed Tensors (the data structure
# used all over the place in Tensorflow), it's like an input to the
# graph/network

# can chain things to make it even more powerful

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b:4.5}))


# Variables allow graph to have trainable parameters
#to set a variable, you execute it in the form: variable= tf.Variable([value1, value2....], type_of_input(ex: tf.float32))
W = tf.Variable([0.3],tf.float32)
b = tf.Variable([-.3],tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x+b
#this command is required to initialize all variables in a tensorflow program
init = tf.global_variables_initializer()
sess.run(init)


#constants are initialized when you call tf.constant
# unlike constants, tf variables are not intialized when you call .Variable
# you must call tf.global_variables_initializer() 

print("The model produces :",sess.run(linear_model,{x:[1,2,3,4]}), "when x:[1,2,3,4]")
# an error function is the same as a loss function 
# y is a placeholder for desired values 

##y = tf.placeholder(tf.float32)
##squared_deltas = tf.square(linear_model - y)
##loss = tf.reduce_sum(squared_deltas)
##print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print("Loss" , sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


###################
#####TRAINING######
###################

#tf.assign reassigns a variable 
#tensorflow provides some Optimizers (i.e. the functions that actually figure
#out the correct values )
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init) # resetting to initial values (I didn't change them though)
for i in range(1000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
print(sess.run([W,b]))


