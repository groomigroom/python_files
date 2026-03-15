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
