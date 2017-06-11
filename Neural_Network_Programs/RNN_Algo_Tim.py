'''
*****************
*Timothy Wroge
*6/11/2017
*Stock Prediction Algorithm 
*Mark 1
*****************
'''



import tensorflow as tf


#initializing variables
#input tensor is size [1, 6]
#[Current Stock Price, Volume, Commodity Price, High, Low , Volitility]
#I initialized it as None so that we could train it batchwise
input_data =tf.placeholder(tf.float32,shape=[None, 6], name="Inputs")
output_prediction=tf.placeholder(tf.float32,shape=[None, 6], name="Prediction")
#this is the tensor for the output prior to regularizing it 
output=tf.placeholder(tf.float32,shape=[None, 6])

#These will be the weights of the hiddenlayers
#initial layer 1
M=50
N=30

#output layer 2
L=20
P=10

#inialize the number of steps so that the model can be optimized through backpropogation
#this will effectively determine the number of data points the model will output before
#it is optimized
number_of_time_steps=20
#batchsize for training data
batch_size=10
def first_multilayer_NN(input_data, M, N, name="first_multilayer_NN"):
    with tf.name_scope(name):
        W1=tf.Variable(tf.truncated_normal([6, M], std=0.1), name="W1")
        b1=tf.Variable(tf.zeros([M]), name="b1")
        W2=tf.Variable(tf.truncated_normal([M, N], std=0.1), name="W2")
        b2=tf.Variable(tf.zeros([M]), name="b2")
        #implementing the network
        y1 = tf.nn.relu(tf.matmul(input_data, W1) + b1)
        y = tf.nn.relu(tf.matmul(y1, W2) + b2)
        return y
    #possible second multilayer NN
'''
def second_multilayer_NN(input_data, N, L, P, name="second_multilayer_NN"):
    with tf.name_scope(name): 
        W3=tf.Variable(tf.truncated_normal([N, L], std=0.1), name="W3")
        b3=tf.Variable(tf.zeros([N]), name="b3")
        W4=tf.Variable(tf.truncated_normal([L, P], std=0.1), name="W4")
        b4=tf.Variable(tf.zeros([P]), name="b4")
        W5=tf.Variable(tf.truncated_normal([P, 6], std=0.1), name="W5")
        b5=tf.Variable(tf.zeros([6]), name="b5")
        #implementing the network
        y3 = tf.nn.relu(tf.matmul(input_data, W3) + b3)
        y4 = tf.nn.relu(tf.matmul(y3, W4) + b4)
        y = tf.nn.softmax(tf.matmul(y4, W5) + b5)
        return y
'''
#defining the intermediate layers
GruCell_one=tf.contrib.rnn.RNNCell
#initialize all variables and initialize session
sess=tf.InteractiveSession()
tf.global_variables_initializer().run()

#tf.summary.FileWriter
# class that writes data for tensorboard
#  create a directory for the summary data
#filewrite_out=tf.summary.Filewriter("/tmp/RNN_algo/1")
#filewrite_out.add_graph(sess.graph)
# to access the tensorboard data enter:
#   >> tensorboard --logdir /tmp/RNN_algo/1

#we can clear up the graph using 'node names' and 'name scopes'
#in each layer part we can add 'name="Whatever you want to call it"'
#  and then call it through
#  with tf.name_scope(name):
#do the same for the training elements like 'train'(for optimizer), 'accuracy'







ouput=second_multilayer_NN(input_data, N, L, P)
output_prediction=tf.multiply(output, input_data)
