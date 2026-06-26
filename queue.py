def isQueueFull() :
    global size, queue, front, rear
    if (rear == size - 1) :
        return True
    else :
        return False

def isQueueEmpty() :
    global size, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data) :
    global size, queue, front, rear
    if (isQueueFull()) :
        print("큐 꽉 참")
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global size, queue, front, rear
    if (isQueueEmpty()) :
        print("큐 빔")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global size, queue, front, rear
    if (isQueueEmpty()) :
        print("큐 빔")
        return None
    return queue[front + 1]

size = int(input("큐의 크기 입력"))
queue = [None for _ in range(size)]
front = rear = -1

if __name__ == "__main__" :
    select = input("삽입(I) / 추출 (E) / 확인 (V) / 종료 (X) 중 하나 선택")

    while (select.upper() != 'X') :
        if select.upper() == 'I' :
            data = input("입력할 데이터")
            enQueue(data)
            print(f"큐 상태 : {queue}")
        elif select.upper() == 'E' :
            data = deQueue()
            print(f"추출된 데이터 : {data}")
            print(f"큐 상태 : {queue}")
        elif select.upper() == 'V' :
            data = peek()
            print(f"확인된 데이터 : {data}")
            print(f"큐 상태 : {queue}")
        else :
            print("??????")

        select = input("삽입(I) / 추출 (E) / 확인 (V) / 종료 (X) 중 하나 선택")

    print("끝끝끝")
