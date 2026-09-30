import tensorflow as tf
import numpy as np
np.__version__

#------------------------------------

number4_tensor = tf.constant(4)
number4_tensor
#<tf.Tensor: shape=(), dtype=int32, numpy=4>
#스칼라, 순위-0 텐서 -> 단일값을 포함하며 축은 없다.

#------------------------------------


rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
rank_1_tensor
#<tf.Tensor: shape=(3,), dtype=float32, numpy=array([2., 3., 4.], dtype=float32)>
#벡터, 순위-1 텐서


#------------------------------------

rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
rank_2_tensor
"""
<tf.Tensor: shape=(3, 2), dtype=float16, numpy=
array([[1., 2.],
       [3., 4.],
       [5., 6.]], dtype=float16)>
       """


#------------------------------------

rank_3_tensor = tf.constant([
  [[0, 1, 2, 3, 4],
   [5, 6, 7, 8, 9]],
  [[10, 11, 12, 13, 14],
   [15, 16, 17, 18, 19]],
  [[20, 21, 22, 23, 24],
   [25, 26, 27, 28, 29]],])
rank_3_tensor

"""
<tf.Tensor: shape=(3, 2, 5), dtype=int32, numpy=
array([[[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9]],

       [[10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19]],

       [[20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29]]], dtype=int32)>

"""

#------------------------------------

#넘파이 배열로 변환하기

rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
np.array(rank_2_tensor)
"""
array([[1., 2.],
       [3., 4.],
       [5., 6.]], dtype=float16)
       """

#------------------------------------


rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
rank_2_tensor.numpy()
"""
array([[1., 2.],
       [3., 4.],
       [5., 6.]], dtype=float16)
"""

#------------------------------------


a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]])
print(tf.add(a, b)) #덧셈
"""
tf.Tensor(
[[2 3]
 [4 5]], shape=(2, 2), dtype=int32)
 """

#------------------------------------

