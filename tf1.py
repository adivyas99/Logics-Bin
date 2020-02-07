# Performing an operation on tensorflow

import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float16, name = "x1")
y = tf.placeholder(tf.float16, name = "y1")

multiply = tf.multiply(x,y,name = "multiply1")

with tf.Session() as sess:
    result = sess.run(multiply, feed_dict={x: [1,3,5], y:[2,4,6] })
print(result)


# To make a pipeline

x_input = np.random.sample((1,2))
print(x_input)

x = tf.placeholder(tf.float32, shape=[1,2], name = 'X')

dataset = tf.data.Dataset.from_tensor_slices(x)

iterator = tf.data.make_initializable_iterator( dataset) 
get_next = iterator.get_next()

with tf.Session() as sess:  
    sess.run(iterator.initializer, feed_dict={ x: x_input })  
    print(sess.run(get_next)) 


#--------------------------------------------
    
# Named my_scalar
r2 = tf.constant(1, tf.int16, name = "my_scalar") 
print(r2)			    
    
# Decimal
r1_decimal = tf.constant(1.12345, tf.float32)
print(r1_decimal)
# String
r1_string = tf.constant("Guru99", tf.string)
print(r1_string)		
    
## Rank 1r1_vector = tf.constant([1,3,5], tf.int16)
print(r1_vector)
r2_boolean = tf.constant([True, True, False], tf.bool)
print(r2_boolean)	

## Rank 3
r3_matrix = tf.constant([ [[1, 2],
                           [3, 4], 
                           [5, 6]] ], tf.int16)
print(r3_matrix)	

# Shape of tensor
m_shape = tf.constant([ [10, 11],
                        [12, 13],
                        [14, 15] ]                      
                     ) 
m_shape.shape			

# Create a vector of 1
print(tf.ones([10, 10]))	

# Create a vector of ones with the same number of rows as m_shape
print(tf.ones(m_shape.shape[0]))			

# Create a vector of ones with the same number of column as m_shape
print(tf.ones(m_shape.shape[1]))

print(m_shape.dtype)

# Change type of data
type_float = tf.constant(3.123456789, tf.float32)
type_int = tf.cast(type_float, dtype=tf.int32)
print(type_float.dtype)
print(type_int.dtype)	

x = tf.constant([2.0], dtype = tf.float32)
print(tf.sqrt(x))	

# Add
tensor_a = tf.constant([[1,2]], dtype = tf.int32)
tensor_b = tf.constant([[3, 4]], dtype = tf.int32)

tensor_add = tf.add(tensor_a, tensor_b)
print(tensor_add)

# Create a Variable
## Create 2 Randomized values
var = tf.get_variable("var", [1, 2])
print(var.shape)			

var_init_1 = tf.get_variable("var_init_1", [1, 2], dtype=tf.int32,  initializer=tf.zeros_initializer)
print(var_init_1.shape)		

# Create a 2x2 matrixtensor_const = tf.constant([[10, 20], [30, 40]])
# Initialize the first value of the tensor equals to tensor_const
var_init_2 = tf.get_variable("var_init_2", dtype=tf.int32,  initializer=tensor_const)
print(var_init_2.shape)	


#--
## Create, run  and evaluate a session
x = tf.constant([2])
y = tf.constant([4])
## Create operator
multiply = tf.multiply(x, y)	
## Create a session to run the code
sess = tf.Session() 
result_1 = sess.run(multiply)
print(result_1)
sess.close()	

with tf.Session() as sess:    
    result_2 = multiply.eval()
print(result_2) 	

## Check the tensors created before
sess = tf.Session()
print(sess.run(r1))
print(sess.run(r2_matrix))
print(sess.run(r3_matrix))	

sess.run(tf.global_variables_initializer())
print(sess.run(var))
print(sess.run(var_init_1))
print(sess.run(var_init_2))	

x = tf.get_variable("x", dtype=tf.int32,  initializer=tf.constant([5]))
z = tf.get_variable("z", dtype=tf.int32,  initializer=tf.constant([6]))
c = tf.constant([5], name =	"constant")
square = tf.constant([2], name =	"square")
f = tf.multiply(x, z) + tf.pow(x, square) + z + c			

init = tf.global_variables_initializer() # prepare to initialize all variables
with tf.Session() as sess:    
    init.run() # Initialize x and y    
    function_result = f.eval()
print(function_result)   
















