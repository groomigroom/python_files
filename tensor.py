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

c = tf.constant([[4.0, 5.0], [10.0, 1.0]])

# Compute the softmax
print(tf.nn.softmax(c))

"""
tf.Tensor(
[[2.6894143e-01 7.3105860e-01]
 [9.9987662e-01 1.2339458e-04]], shape=(2, 2), dtype=float32)

"""

"""
공동 연구원처럼 친절하고 정확하게 설명해 드릴게요!
제시해주신 텐서플로(TensorFlow) 코드에서 해당 출력값이 나오는 이유는 tf.nn.softmax() 함수가 행(Row) 단위로 소프트맥스(Softmax) 연산을 수행하기 때문입니다.
소프트맥스는 각 행의 숫자들을 0과 1 사이의 확률 값으로 변환하며, 변환된 한 행의 합은 항상 1이 됩니다.
------------------------------
## 1. 소프트맥스(Softmax) 공식
어떤 행의 입력 값들이 $x_1, x_2$ 일 때, 소프트맥스 값은 다음과 같이 계산됩니다.
$$\text{Softmax}(x_i) = \frac{e^{x_i}}{\sum e^{x}}$$ 
즉, 각 원소에 자연상수 $e$의 거듭제곱(지수 함수)을 취한 뒤, 그 값들의 총합으로 나누어 비율을 구하는 방식입니다.
------------------------------
## 2. 한 행씩 직접 계산해보기## 📌 첫 번째 행: [4.0, 5.0]

   1. 지수 함수 적용 ($e^x$):
   * $e^{4.0} \approx 54.598$
      * $e^{5.0} \approx 148.413$
   2. 지수의 총합 구하기:
   * $54.598 + 148.413 = 203.011$
   3. 각 값을 총합으로 나누기:
   * 첫 번째 원소: $\frac{54.598}{203.011} \approx$ 0.26894 ($2.6894 \times 10^{-1}$)
      * 두 번째 원소: $\frac{148.413}{203.011} \approx$ 0.73105 ($7.3105 \times 10^{-1}$)
   
결과적으로 [0.26894, 0.73105]가 되며, 두 값을 더하면 정확히 1.0이 됩니다.
## 📌 두 번째 행: [10.0, 1.0]

   1. 지수 함수 적용 ($e^x$):
   * $e^{10.0} \approx 22026.466$
      * $e^{1.0} \approx 2.718$
   2. 지수의 총합 구하기:
   * $22026.466 + 2.718 = 22029.184$
   3. 각 값을 총합으로 나누기:
   * 첫 번째 원소: $\frac{22026.466}{22029.184} \approx$ 0.99987
      * 두 번째 원소: $\frac{2.718}{22029.184} \approx$ 0.00012339 ($1.2339 \times 10^{-4}$)
   
두 번째 행은 두 값의 차이(10과 1)가 크다 보니, 지수 함수를 거치면서 앞의 숫자가 지배적으로 커져 0.99987이라는 1에 매우 가까운 확률을 갖게 됩니다.
------------------------------
## 💡 3줄 요약

* 소프트맥스는 각 행을 확률 분포(합이 1)로 만들어 줍니다.
* 값이 클수록 지수 함수($e^x$) 특성상 출력 확률이 폭발적으로 증가합니다.
* 출력에 표시된 e-01은 $10^{-1}$, e-04는 $10^{-4}$를 뜻하는 부동소수점 과학적 표기법입니다.

딥러닝 모델을 구현 중이신가요? 만약 행 단위(axis=-1)가 아니라 열 단위(axis=0)나 전체를 기준으로 소프트맥스를 계산하고 싶으시다면, 축 설정을 변경하는 방법을 안내해 드릴 수 있습니다. 필요하시면 말씀해 주세요!


"""

#------------


tf.convert_to_tensor([1,2,3])
#<tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 2, 3], dtype=int32)>


#------------

tf.reduce_max([1,2,3])
#<tf.Tensor: shape=(), dtype=int32, numpy=3> -> 최대값 tensor로 반환

#------------

tf.reduce_max(np.array([1,2,3]))
#<tf.Tensor: shape=(), dtype=int64, numpy=3> -> 최대값 tensor로 반환

#------------


rank_4_tensor = tf.zeros([3, 2, 4, 5])
rank_4_tensor
"""
<tf.Tensor: shape=(3, 2, 4, 5), dtype=float32, numpy=
array([[[[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]],

        [[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]]],


       [[[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]],

        [[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]]],


       [[[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]],

        [[0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0.]]]], dtype=float32)>
         """

#-------------------------------------


rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Type of every element:", rank_4_tensor.dtype)
#Type of every element: <dtype: 'float32'>

#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Number of axes:", rank_4_tensor.ndim)
#Number of axes: 4
#차원의 개수를 의미 


#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Shape of tensor:", rank_4_tensor.shape)
#Shape of tensor: (3, 2, 4, 5)


#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
#Elements along axis 0 of tensor: 3

#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Elements along the last axis of tensor:", rank_4_tensor.shape[-1])
#Elements along the last axis of tensor: 5

#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy())
#Total number of elements (3*2*4*5):  120

#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
tf.rank(rank_4_tensor)
#<tf.Tensor: shape=(), dtype=int32, numpy=4>



#-------------------------------------

rank_4_tensor = tf.zeros([3, 2, 4, 5])
tf.shape(rank_4_tensor)
#<tf.Tensor: shape=(4,), dtype=int32, numpy=array([3, 2, 4, 5], dtype=int32)>

#-------------------------------------

rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(rank_1_tensor.numpy())
#[ 0  1  1  2  3  5  8 13 21 34]
print("First:", rank_1_tensor[0].numpy())
print("Second:", rank_1_tensor[1].numpy())
print("Last:", rank_1_tensor[-1].numpy())
"""
First: 0
Second: 1
Last: 34
"""

#-------------------------------------

rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print("Everything:", rank_1_tensor[:].numpy())
print("Before 4:", rank_1_tensor[:4].numpy())
print("From 4 to the end:", rank_1_tensor[4:].numpy())
print("From 2, before 7:", rank_1_tensor[2:7].numpy())
print("Every other item:", rank_1_tensor[::2].numpy())
print("Reversed:", rank_1_tensor[::-1].numpy())
"""
Everything: [ 0  1  1  2  3  5  8 13 21 34]
Before 4: [0 1 1 2]
From 4 to the end: [ 3  5  8 13 21 34]
From 2, before 7: [1 2 3 5 8]
Every other item: [ 0  1  3  8 21]
Reversed: [34 21 13  8  5  3  2  1  1  0]
"""


#-------------------------------------

rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(rank_2_tensor.numpy())
"""
[[1. 2.]
 [3. 4.]
 [5. 6.]]
 """



#-------------------------------------

rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(rank_2_tensor[1, 1].numpy())
#4.0
print("Second row:", rank_2_tensor[1, :].numpy())
print("Second column:", rank_2_tensor[:, 1].numpy())
print("Last row:", rank_2_tensor[-1, :].numpy())
print("First item in last column:", rank_2_tensor[0, -1].numpy())
print("Skip the first row:")
print(rank_2_tensor[1:, :].numpy(), "\n")
"""
4.0
Second row: [3. 4.]
Second column: [2. 4. 6.]
Last row: [5. 6.]
First item in last column: 2.0
Skip the first row:
[[3. 4.]
 [5. 6.]] 
"""



#-------------------------------------

rank_3_tensor = tf.constant([
  [[0, 1, 2, 3, 4],
   [5, 6, 7, 8, 9]],
  [[10, 11, 12, 13, 14],
   [15, 16, 17, 18, 19]],
  [[20, 21, 22, 23, 24],
   [25, 26, 27, 28, 29]],])
print(rank_3_tensor[:, :, 4])
"""
tf.Tensor(
[[ 4  9]
 [14 19]
 [24 29]], shape=(3, 2), dtype=int32)
 """


#-------------------------------------


x = tf.constant([[1], [2], [3]])
print(x.shape.as_list())
#[3, 1]

#-------------------------------------

x = tf.constant([[1], [2], [3]])
reshaped = tf.reshape(x, [1, 3])
reshaped
#<tf.Tensor: shape=(1, 3), dtype=int32, numpy=array([[1, 2, 3]], dtype=int32)>


#-------------------------------------




#-------------------------------------




인덱싱
https://www.tensorflow.org/guide/tensor?hl=ko
