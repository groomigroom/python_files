stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "김구름"
print(stack)
top += 1
stack[top] = "비숑"
top += 1
stack[top] = "구름씨"
top += 1
stack[top] = "구름구름"
top += 1
stack[top] = "김구름이"


print("스택 상태는")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])
