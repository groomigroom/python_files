import random

lottoList = []

def lottoFunc() :
    lottoNum = random.randint(1, 45)
    return lottoNum

while True :
    num = lottoFunc()

    if num in  lottoList :
        continue
    else :
        lottoList.append(num)
    if len(lottoList) == 6 :
        break

lottoList.sort()
print(lottoList)


#--------------------------


def test() :
    global a
    a = 20

# test()
print(a)


#-------------------

import datetime

now = datetime.datetime.now()
print(now)
print(now + datetime.timedelta(days = 100))
#몇일 후인지 더해주는거
print(now + datetime.timedelta(hours = 3))
print(now + datetime.timedelta(weeks = 2))


#----------------------------

from datetime import datetime, timedelta

def getCurrent() :
    currentD = datetime.now()
    return currentD

def getAfterDate(currentD, day) :
    retDate = currentD + timedelta(days=day)
    return retDate

nowDay = getCurrent()
hundredDay = getAfterDate(nowDay, 100)

print(f"현재 날짜와 시간 ==> {nowDay}")
print(f"100일 후의 날짜와 시간 ==> {hundredDay}")

#----------------------------

def funcLen(pwd) :
    if len(pwd) < 8:
        return False

    if pwd.isalnum():
        #알파벳과 숫자로만 이루어져 있나 검사하는 거
        return True
    else :
        return False

password = input("비번 입력")

if funcLen(password) :
    print("정확한 비번")
else :
    print("비번 다시 생성")

#---------------------

def funcLen(pwd) :
    if len(pwd) < 8:
        return False

    if pwd.isalnum():
        #알파벳과 숫자로만 이루어져 있나 검사하는 거
        return True
    else :
        return False

while(True) :
    password = input("비번 입력")

    if funcLen(password) :
        print("정확한 비번")
        break
    else :
        print("비번 다시 생성")

#-------------------


def funcLen(pwd) :
    if len(pwd) < 8:
        return False

    if pwd.isalnum():
        #알파벳과 숫자로만 이루어져 있나 검사하는 거
        return True
    else :
        return False

cnt = 0

while(cnt < 3) :
    password = input(f"현재{cnt + 1}회: 비번 입력 기회 3번")

    if funcLen(password) :
        print("정확한 비번")
        break
    else :
        print("비번 다시 생성")

    cnt += 1


#----------------------------

def multi_func(var1, var2, var3 = 1) :
    result = var1 * var2 * var3
    return result

aa = multi_func(4, 2)
bb = multi_func(4, 2, 3)
print(aa, bb)

#-----------------

def myFunc() :
    retValue = 100
    return retValue

myFunc()
print(retValue)

#이거 에러뜸0000000000000000000000000

#------------------------



def Calc(a, b) :
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

a = int(input("숫자 1 ==>"))
b = int(input("숫자 1 ==>"))
Calc(a, b)

#------------------------


def Calc(a, b) :
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

a = int(input("숫자 1 ==>"))
b = int(input("숫자 1 ==>"))
Calc(a, b)

#이제 위 계산기를 변형해서 출력값을 2진수 형식으로 변형해서 나오는 것과 16진수 형식으로 변형해서 나오는 것과
#8진수로 변형해서 나오는 것으로 수정 후
#숫자를 1개 더 받아서 또 계산기를 돌리는 프로그램으로 수정 부탁드립니다.

#---------------------------

infile = None
inStr = ''
infile = open("E:/gongbu.txt", "r", encoding = 'utf-8')
#읽기여서 r

inStr = infile.readline()
print(inStr)

infile.close()


#------------------



infile = None
inStr = ''
infile = open("E:/gongbu.txt", "r", encoding = 'utf-8')
#읽기여서 r

for i in range(3):
    inStr = infile.readline()
    print(inStr)
    #한 줄씩 읽는 거


infile.close()

#----------------------

infile = None
inStrs = []
infile = open("E:/gongbu.txt", "r", encoding = 'utf-8')


inStrs = infile.readlines()
print(inStrs)

infile.close()


#----------------------

infile = None
inStrs = []
infile = open("E:/gongbu.txt", "r", encoding = 'utf-8')


inStrs = infile.readlines()

ii = 1

for i in inStrs :
    print(f"{ii}: {i}", end = "")
    ii += 1

infile.close()


#------------------------

infile = None

infile = open("E:/gongbu22.txt", "w")

outStr = "김구름 멍멍"
infile.writelines(outStr + "\n")
outStr = "김구름 멍멍멍"
infile.writelines(outStr + "\n")
outStr = "김구름 멍멍멍2222"
infile.writelines(outStr + "\n")

infile.close()

#파일 생성 후 글 써주는 거


#-------------------------------
