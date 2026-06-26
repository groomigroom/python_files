def isStackFull() :
    global size, stack, top
    if (top >= size - 1) :
        return True
    else :
        return False
    
def isStackEmpty() :
    global size, stack, top
    if (top == -1) :
        return True
    else :
        return False

def push(data) :
    global size, stack, top
    if(isStackFull()) :
        print("스택이 가득 찼다.")
        return
    top = top + 1
    stack[top] = data

def pop() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었다.")
        return None
    data = stack[top]
    stack[top] = None
    top = top - 1
    return data

def peek() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었다.")
        return None
    return stack[top]

#전역 변수 선언
size = int(input("스택의 크기 입력하기"))
stack = [None for _ in range(size)]
top = -1

if __name__ == "__main__" :
    select = input("\n삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나 선택하기")

    while(select.upper() != 'X') :
        if select.upper() == 'I' :
            data = input("입력할 데이터")
            push(data)
            print(f"스택 상태: {stack}")
        elif select.upper() == 'E' :
            data = pop()
            print(f"추출된 데이터: {data}")
            print(f"스택 상태: {stack}")
        elif select.upper() == 'V' :
            data = peek()
            print(f"확인된 데이터: {data}")
            print(f"스택 상태: {stack}")
        else :
            print("입력이 잘못됨")

        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) 중 하나 선택하기")

    print("프로그램 끝")
