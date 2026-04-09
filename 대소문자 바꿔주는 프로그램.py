#str1 = "Python"
str1 = input("대소문자 섞어서 입력하기")

print(f"원본은 {str1}입니다.")
print(f"반대 문자열은", end = "")
for i in range(len(str1)):
    if str1[i].isupper():
        print(str1[i].lower(), end = "")
    else :
        print(str1[i].upper(), end = "")

