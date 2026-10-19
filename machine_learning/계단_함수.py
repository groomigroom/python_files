import numpy as np
import matplotlib.pyplot as plt
def step(x):
    return np.array(x > 0, dtype=np.int32)
x = np.arange(-5.0, 5.0, 0.1) # -5.0부터 5.0까지 0.1 간격 생성
y = step(x)
plt.title('Step Function')
plt.plot(x,y)
plt.show()
