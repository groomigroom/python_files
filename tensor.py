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

#---------

c = tf.constant([[4.0, 5.0], [10.0, 1.0]])

# Find the index of the largest value
print(tf.math.argmax(c))

"""

tf.Tensor([1 0], shape=(2,), dtype=int64)
"""

#-----------

"""
TensorFlow의 tf.nn.softmax는 모델이 출력한 실수 값(Logits)을 0과 1 사이의 확률 값으로 변환해 주는 함수입니다.
주로 딥러닝에서 다중 클래스 분류(Multi-class Classification) 문제를 해결할 때, 최종 출력층(Output Layer)의 활성화 함수로 사용됩니다. 변환된 결과값들의 총합은 항상 1이 되는 것이 가장 큰 특징입니다.
------------------------------
## 📌 왜 굳이 Softmax를 사용할까요?
모델의 최종 출력값(점수)이 [2.0, 1.0, 0.1]로 나왔다고 가정해 보겠습니다. 이 점수만으로는 다음과 같은 한계가 있습니다.

   1. 점수의 범위가 정해져 있지 않아 직관적이지 않습니다.
   2. "첫 번째 클래스일 확률이 두 번째보다 얼마나 더 높은가?"를 확률적으로 표현하기 어렵다.

이 값에 tf.nn.softmax를 적용하면 다음과 같이 변환됩니다.

import tensorflow as tf
logits = tf.constant([2.0, 1.0, 0.1])probabilities = tf.nn.softmax(logits)

print(probabilities.numpy())# 결과: [0.6590012, 0.24243298, 0.09856581]


* 확률로 변환: 2.0은 약 65.9%, 1.0은 약 24.2%, 0.1은 약 9.8%의 확률로 깔끔하게 정규화됩니다.
* 총합은 1: 세 확률을 모두 더하면 정확히 1.0(100%)이 됩니다.

------------------------------
## 💡 Softmax의 핵심 작동 원리
수식은 간단하게 "각 숫자에 자연상수 e를 거듭제곱한 뒤, 그 값들의 총합으로 나누는 것"입니다. 이 과정에서 두 가지 중요한 효과가 발생합니다.

   1. 지수 함수($e^x$)의 효과 (Soft + Max):
   * 입력값 중 가장 큰 값을 더 도드라지게(Max) 만들어 줍니다.
      * 하지만 완전히 하나만 고르는 Hard Max(예: [1, 0, 0])와 달리, 나머지 작은 값들에게도 미소한 확률을 남겨두는 부드러운(Soft) 특성을 가집니다. 그래서 이름이 Softmax입니다.
   2. 음수 처리: 지수 함수를 통과하면 아무리 작은 음수(-5.0 등)라도 항상 0보다 큰 양수가 되므로, 안정적인 확률 분포를 만들 수 있습니다.

------------------------------
## ⚙️ axis(축) 매개변수
입력 데이터가 2차원(예: [배치 크기, 클래스 개수]) 이상일 때는 어떤 축을 기준으로 확률을 계산할지 axis를 지정해야 합니다. 기본값은 가장 마지막 차원인 axis=-1입니다.

# 2개의 데이터(배치)가 각각 3개의 클래스 점수를 가질 때logits = tf.constant([[2.0, 1.0, 0.1],
                      [1.0, 3.0, 0.2]])
# 각 행(가로 방향) 안에서 확률의 합이 1이 되도록 계산
print(tf.nn.softmax(logits, axis=-1))

현재 풀고 계신 문제가 분류해야 할 클래스가 여러 개인 다중 분류인가요? 만약 정답이 두 가지만 있는 이진 분류(Binary Classification)라면 softmax 대신 sigmoid를 사용하는 것이 더 효율적일 수 있습니다. 어떤 문제를 해결 중이신지 들려주시면 알맞은 함수를 추천해 드릴게요!

"""