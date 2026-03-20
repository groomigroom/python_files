#함수 정의 내용입니다.
def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False

print (is_even(1))
print (is_even(4))
print (is_even(7))

#####

def calc(x, y):
	
	x *= 3
	y /= 3
	print(x, y)
	return x

a, b = 3, 12
a = calc(a, b)

print(a, b)

