class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
"""
Animal이라는 클래스(설계도)를 정의하고, 객체(인스턴스)가 생성될 때 이름(name)과 몸무게(weight)라는 속성(데이터)을 자동으로 초기화(설정)하는 생성자(Constructor) 메소드입니다.

class Animal:: Animal이라는 이름의 새로운 객체 지향 클래스를 정의합니다.
def __init__(self, ...):: 파이썬의 특수 메소드(매직 메소드)인 생성자입니다. Animal() 형태로 객체를 만들 때 자동으로 호출되어 초기 설정을 담당합니다.
self: 생성되는 객체(인스턴스) 자기 자신을 가리킵니다.
self.name = name: 객체 고유의 속성인 name에 전달받은 매개변수 name의 값을 할당합니다. 
"""


animals = [
    Animal("dog", 2),
    Animal("cat", 1),
    Animal("pig", 4),
    Animal("cow", 5),
    None
]
#대괄호는 리스트

index = 0

def getAnimal():
    global index
    animal = animals[index]
    index += 1
    return animal


def main():
    truck = []
    fence = []
    truck_weight = 0

    while True:
        animal = getAnimal()

        if animal is None:
            break

        if truck_weight + animal.weight <= 7:
            truck.append(animal)
            truck_weight += animal.weight
        else:
            fence.append(animal)

    return truck, fence


truck, fence = main()

print("Truck:", [a.name for a in truck])
print("Fence:", [a.name for a in fence])

"""
`def main():`은 **프로그램의 핵심 로직을 실행하는 함수**입니다. 이 함수는 **animals 리스트에서 동물을 하나씩 가져와 트럭(truck)에 태우거나 울타리(fence)로 보내는 작업**을 합니다.
동작 원리를 **순서대로** 설명하면 다음과 같습니다. 🚚🐄

---

## 1️⃣ 변수 초기화

```python
truck = []
fence = []
truck_weight = 0
```

* `truck = []` → 트럭에 실을 동물들을 저장할 **리스트**
* `fence = []` → 트럭에 못 실은 동물들을 넣을 **리스트**
* `truck_weight = 0` → 트럭에 실린 동물들의 **현재 총 무게**

---

## 2️⃣ 무한 반복 시작

```python
while True:
```

* `True`이므로 **계속 반복**합니다.
* 단, 특정 조건에서 `break`로 반복을 종료합니다.

---

## 3️⃣ 동물 하나 가져오기

```python
animal = getAnimal()
```

`getAnimal()` 함수는

1. `animals[index]`에서 동물을 하나 가져오고
2. `index`를 1 증가시키고
3. 그 동물을 반환합니다.

즉 **리스트에서 순서대로 동물을 꺼내는 역할**입니다.

꺼내지는 순서:

```
dog → cat → pig → cow → None
```

---

## 4️⃣ 종료 조건 확인

```python
if animal is None:
    break
```

리스트 마지막에 `None`이 있으므로
이 값이 나오면 **더 이상 동물이 없다고 판단하고 반복 종료**합니다.

---

## 5️⃣ 트럭에 실을 수 있는지 확인

```python
if truck_weight + animal.weight <= 7:
```

트럭 **최대 무게 = 7**

현재 트럭 무게 + 새 동물 무게가
**7 이하이면 트럭에 실습니다.**

---

## 6️⃣ 트럭에 싣기

```python
truck.append(animal)
truck_weight += animal.weight
```

* `append()` → 리스트에 동물 추가
* `truck_weight` → 동물 무게만큼 증가

---

## 7️⃣ 트럭에 못 싣는 경우

```python
else:
    fence.append(animal)
```

무게 초과라면 **울타리(fence)로 보냅니다.**

---

# 실제 실행 과정

동물 목록:

```
dog(2), cat(1), pig(4), cow(5)
트럭 최대 무게 = 7
```

### 1️⃣ dog (2)

```
0 + 2 <= 7 → 트럭
truck = [dog]
weight = 2
```

### 2️⃣ cat (1)

```
2 + 1 <= 7 → 트럭
truck = [dog, cat]
weight = 3
```

### 3️⃣ pig (4)

```
3 + 4 <= 7 → 트럭
truck = [dog, cat, pig]
weight = 7
```

### 4️⃣ cow (5)

```
7 + 5 > 7 → fence
fence = [cow]
```

### 5️⃣ None

```
반복 종료
```

---

# 최종 결과

```python
Truck: ['dog', 'cat', 'pig']
Fence: ['cow']
```

---

✅ **정리**

`main()` 함수의 역할

1. 동물을 하나씩 가져온다 (`getAnimal()`)
2. 트럭 무게를 확인한다
3. 실을 수 있으면 `truck`
4. 못 실으면 `fence`
5. `None`이 나오면 종료
6. 두 리스트를 반환

```python
return truck, fence
```

---

원하시면 이 코드에서 **왜 `global index`가 필요한지**도 아주 쉽게 설명해 드리겠습니다. (파이썬에서 많이 헷갈리는 부분입니다)
"""
