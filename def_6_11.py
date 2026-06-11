myList = []
for i in range(0, 100) :
    myList.append(0)
print(myList)

----------------------------


myList = [100, 200, 300, 400, 500]
hap = 0
for i in range(0, 5) :
    hap += myList[i]

print(hap)

-----------------------

myList = [100, 200, 300, 400, 500]
hap = 0
for i in myList :
    hap += i

print(hap)

-------------------------


myList = [100, 200, 300, 400, 500]
myList.sort(reverse=1)
print(myList)


----------------------------


triples = ("이지우", "서다현", "코토네")
triples[1] = "서아"


#이렇게 하면 안됨

---------------------------------

triples = {1: "이지우", 2: "코토네", 3: "정병기"}
#print(triples[0]) 이건 안됨
print(triples[1])
print(triples.keys())
print(triples.values())
print(triples.items())
#print(triples.items()[0]) 이건 안됨
triplesList = list(triples.items())
print(triplesList[0])




----------------------------

import random

diceList = []
diceHap = 0

for i in range(100) :
    dd = random.randint(1, 6)
    diceList.append(dd)
    diceHap += dd

diceAvg = diceHap / len(diceList)
print(diceList)
print(f"평균은 {diceAvg}이다.")

-----------------

hap = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for f in range(빈칸):
                hap += 1

print(hap)
#출력값이 625가 되게 하는 빈칸에 들어갈 수는?


-----------------

def 공부() :
    print("공부합시다.")
    print("공부합시다.")

공부()

------------------


def hobby(person) :
    print(f"{person}의 취미는 공부입니다.")

hobby("박형주")
hobby("박형주")

-------------------------

def hobby(person, hobby) :
    print(f"{person}의 취미는 {hobby}입니다.")

hobby("박형주", "공부")
hobby("박형주", "과제")

-----------------------

def cmto():
    
    print(f"{lenCm}cm는 {lenCm * 0.393701}인치이다.")

lenCm = float(input("길이 cm로 입력"))
cmto()


-------------------------------------------------

def mungmung() :
    print(f"멍멍이는 {구름이}입니다.")

구름이 = input("멍멍이는")
mungmung()


------------------------

def nono() :
    pass

nono()


----------------------

def gongbu1() :
    print("공부합시다.11")
def gongbu2() :
    print("공부합시다.22")
def gongbu3() :
    print("공부합시다.33")
def gongbu4() :
    print("공부합시다.44")
def gongbu5() :
    print("공부합시다.55")
def gongbu6():
    gongbu1()
    gongbu2()
    gongbu3()
    gongbu4()
    gongbu5()

gongbu6()

-------------------------------

def gongbu1() :
    gongbu7()
    print("공부합시다.11")
def gongbu2() :
    print("공부합시다.22")
def gongbu3() :
    print("공부합시다.33")
def gongbu4() :
    print("공부합시다.44")
def gongbu5() :
    print("공부합시다.55")
def gongbu6():
    gongbu1()
    gongbu2()
    gongbu8()
    gongbu3()
    gongbu4()
    gongbu5()
def gongbu7() :
    print("공부합시다.공부합시다.")
def gongbu8() :
    print("공부합시다.공부합시다.공부합시다.공부합시다.공부합시다.공부합시다.공부합시다.공부합시다.")

gongbu6()

---------

def hello(insa) :
    if (insa == "강아지") or (insa == "구름이") :
        print("멍멍")
    elif (insa == "고양이") :
        print("야옹")
    else :
        print("안녕하세요")

hello("강아지")
hello("구름이")
hello("고양이")
hello("인간")

--------------------

def hapfunc() :
    num1 = int(input("정수1"))
    num2 = int(input("정수2"))
    return num1 + num2

print("두 숫자 입력")
hap = hapfunc()
print(hap)

---------------------

def plus(v1, v2) :
    result = 0
    result = v1 + v2
    return result

hap = 0

hap = plus(100, 200)
print(f"100 + 200 = {hap}")


----------------------------


def plus(v1, v2) :
    result = 0
    result = v1 + v2
    if result > 100 :
        return result
    else :
        return result / 2

hap = 0

hap = plus(100, 200)
print(f"100 + 200 = {hap}")

hap = plus(2, 3)
print(hap)


--------------------------


def plus(v1, v2) :
    result = 0
    result = v1 + v2
    if result > 100 :
        return result
    else :
        return result / 2

hap = 0

hap = plus(100, 200)
print(f"100 + 200 = {hap}")

hap = plus(2, 3)
print(hap)
print(plus(3, 440))


------------------------------------------------------

def numnum(v1, v2, v3, v4, v5, v6, v7=11) :
    return v1 * v2 + v3 / v4 * v5 - v6 + v7

a = numnum(1, 2, 3, 4, 5, 6)
b = numnum(1, 2, 3, 4, 5, 6, 112)
print(a, b)
#매개변수가 없을 때 기본값 설정 가능.

----------------------------------------

def groomi(groom) :
    print(f"{groom} 멍멍멍")
    return #반환값 없을 때 걍 적어도 됨. 
    
groomi("kimgroom")


-----------------------

def func3() :
    result1 = 100
    result2 = 200
    return result1, result2

hap1, hap2 = 0, 0
hap1, hap2 = func3()
print(hap1, hap2)


----------------------------


