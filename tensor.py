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

a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]])
print(tf.multiply(a, b)) #곱셈
"""
tf.Tensor(
[[1 2]
 [3 4]], shape=(2, 2), dtype=int32)
 """

#------------------------------------


a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]])
print(tf.matmul(a, b)) #행렬 곱셈

"""

tf.Tensor(
[[3 3]
 [7 7]], shape=(2, 2), dtype=int32)

1행 1열: 앞 행렬의 1행 \((a, b)\) \[\times \] 뒤 행렬의 1열 \((p, r)\) \[\rightarrow \] \(ap + br\)
1행 2열: 앞 행렬의 1행 \((a, b)\) \[\times \] 뒤 행렬의 2열 \((q, s)\) \[\rightarrow \] \(aq + bs\)
2행 1열: 앞 행렬의 2행 \((c, d)\) \[\times \] 뒤 행렬의 1열 \((p, r)\) \[\rightarrow \] \(cp + dr\)
2행 2열: 앞 행렬의 2행 \((c, d)\) \[\times \] 뒤 행렬의 2열 \((q, s)\) \[\rightarrow \] \(cq + ds\)
"""

#------------------------------------

a = tf.constant([[1, 2],
                 [3, 4]])
b = tf.constant([[1, 1],
                 [1, 1]])
print(a + b, "\n") # element-wise addition
print(a * b, "\n") # element-wise multiplication
print(a @ b, "\n") # matrix multiplication

"""
tf.Tensor(
[[2 3]
 [4 5]], shape=(2, 2), dtype=int32) 

tf.Tensor(
[[1 2]
 [3 4]], shape=(2, 2), dtype=int32) 

tf.Tensor(
[[3 3]
 [7 7]], shape=(2, 2), dtype=int32) 
"""

#----------------------

"""
TensorFlow의 tf.reduce_max는 텐서(Tensor)의 차원을 줄이면서 지정한 축(axis)을 기준으로 가장 큰 최댓값을 찾는 함수입니다.
여기서 'reduce(줄이다)'라는 단어가 붙은 이유는 최댓값을 찾으면서 연산에 사용된 차원이 사라지거나 크기가 1로 줄어들기 때문입니다.
"""


c = tf.constant([[4.0, 5.0], [10.0, 1.0]])

# Find the largest value
print(tf.reduce_max(c))


"""
tf.Tensor(10.0, shape=(), dtype=float32)
"""
