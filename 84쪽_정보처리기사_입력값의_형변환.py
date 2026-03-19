a = int(input())
b = float(input())
print(a, b)

c, d = map(int, input().split())
e, f = map(float, input().split())

print(c, d, e, f)

"""
input(): 사용자로부터 한 줄의 문자열을 입력받습니다.
.split(): 입력받은 문자열을 공백(스페이스, 탭 등)을 기준으로 나누어 리스트로 만듭니다.
map(int, ...): 리스트의 모든 요소에 int() 함수를 적용하여 문자열을 정수로 변환합니다.
c, d = ...: 변환된 값들을 차례대로 c와 d에 할당합니다 (언패킹)
"""
