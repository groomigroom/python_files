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
