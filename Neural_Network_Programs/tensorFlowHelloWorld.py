
import tensorflow as tf

#building a graph
#we will begin by working through source operations
#for example:
a = tf.constant([3])
b=tf.constant([2])
#this is the simple adding operation
a_and_b_added1 = tf.add(a, b)
a_and_b_added2 = a+b


#then tensorflow needs to initialize a session to run the code
#these sessions are like creating context for creating a graph inside tensorflow
# sess= tf.Session()
#
# #this will get the result from the code above
# result =sess.run(a_and_b_added2)


# print(result)

#in order to avoid having to close sessions every time, we define them with a "with" block
#after running the with session, it will close automatically
with tf.Session() as sess:
    result=sess.run(a_and_b_added1)
    print(result)
    #after running this block, the session will close automatically

#this portion of the code will go over tensors, variables and placeholders




Scalar=tf.constant([2])
Vector=tf.constant([5,6,2])
Matrix=tf.constant([1,2,3], [2,3,4],[3,4,5])
Tensor=tf.constant([[1,1],[2,2]],[[3,3],[4,4]],[[5,5],[6,6]])



#operations in tensorflow
Matrix_one=tf.constant([1,2],[3,4])
Matrix_two=tf.constant([2,3],[4,5])


#matrix multiplication
first_operation=tf.matmul(Matrix_one, Matrix_two)


#defining variables:
#to use variables, you need to initialize them before the graph is in session
state=tf.Variable(0)

