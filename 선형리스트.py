triples = ["윤서연", "정혜린", "이지우", "김채연", "김유연", "김수민", "김나경", "공유빈", "카에데", "서다현", "코토네", "곽연지", "니엔", "박소현", "신위", "마유", "린", "주빈", "정하연", "박시온", "김채원", "설린", "서아", "지연"]
print(triples)
print(triples[2])

#추가
tri_one = ["윤서연", "정혜린", "이지우", "김채연"]
tri_one.append("코토네")
print(tri_one)
print(tri_one[4])

#선형 리스트 제거 방
tri_one[1] = None
print(tri_one)
tri_one[1] = tri_one[2]
tri_one[2] = tri_one[3]
tri_one[3] = tri_one[4]
del(tri_one[4])
print(tri_one)

no_list = []

def add_data(friend) :
    no_list.append(None)
    nolen = len(no_list)
    no_list[nolen - 1] = friend

add_data("이지우")
add_data("코토네")
add_data("공유빈")
print(no_list)


#------------------

new_unit = []

def add_member(mem) :
    new_unit.append(None)
    ulen = len(new_unit)
    new_unit[ulen - 1] = mem

add_member("윤서연")
add_member("정혜린")
add_member("이지우")
add_member("김채연")
print(new_unit)

#---------------


def add_member(mem) :
    new_unit.append(None)
    ulen = len(new_unit)
    new_unit[ulen - 1] = mem

def insert_member(position, mem) :
    if position < 0 or position > len(new_unit) :
        print("멤버 추가 불가능")
        return
    
    new_unit.append(None)
    ulen = len(new_unit)
    for i in range (ulen - 1, position, -1) :
        new_unit[i] = new_unit[i - 1]
        new_unit[i - 1] = None

    new_unit[position] = mem

def del_member(position) :
    if position < 0 or position > len(new_unit) :
        print("멤버 삭제 불가능")
        return
    
    ulen = len(new_unit)
    new_unit[position] = None

    for i in range (position + 1, ulen) :
        new_unit[i - 1] = new_unit[i]
        new_unit[i] = None

    del(new_unit[ulen - 1])

new_unit = []
select = -1

if __name__ == "__main__" :
    while select != 4 :
        select = int(input("선택하세요: 1.추가 2.삽입 3.삭제 4.종료"))

        if (select == 1) :
            mem = input("추가할 멤버")
            add_member(mem)
            print(new_unit)
        elif (select == 2) :
            pos = int(input("멤버 순서 위치"))
            mem = input("추가할 멤버")
            insert_member(pos, mem)
            print(new_unit)
        elif (select == 3) :
            pos = int(input("쉬기로 한 멤버의 순서?"))
            del_member(pos)
            print(new_unit)
        elif (select == 4) :
            print(new_unit)
            break
        else :
            print("똑바로 입력하세요")
            continue
