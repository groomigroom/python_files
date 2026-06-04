triples_dict = {'메보': '서다현', '서브메보': '이지우', '메인래퍼': '코토네', '1번': '윤서연'}
print(triples_dict)

triples_dict['막내'] = '서아'
print(triples_dict)
print(triples_dict['서브메보'])
triples_dict['멤버수'] = 23
triples_dict['멤버수'] = 24
print(triples_dict)
del triples_dict['멤버수']
print(triples_dict)
print(triples_dict.keys())
print(triples_dict.values())
for i in triples_dict.keys() :
    print(triples_dict[i])

---------------------

score = {'강아지 간식': 'A', '강아지 집': 'B+', '강아지 칫솔': 'C', '강아지 장난감': 'B'}
print(score)

print("\n강아지 간식 시나리오")
print(score['강아지 간식'])
print(score.keys())
score['강아지의 하루'] = 'A+'
score['강아지 멍멍'] = 'A+'
print(score)
score['강아지 멍멍'] = 'AA++'
print(score)

for i in score.keys() :
    print(f"{i} : {score[i]}")


-----------------------

score = {'강아지 간식': '99', '강아지 집': '77', '강아지 칫솔': '88', '강아지 장난감': '111'}
sc_plus = 0

for i in score.keys() :
    sc_plus += int(score[i])

sc_avg = sc_plus / len(score)
print(f"합: {sc_plus}, 평균: {sc_avg}")


-----------------------

score = {'강아지 간식': 99, '강아지 집': 77, '강아지 칫솔': 88, '강아지 장난감': 111}
score['강아지 간식'] += 1
print(score)
print(score.items())
#이거는 키와 밸류를 튜플로 묶어서 출력해 줌.
score_list = list(score.items())
print(score_list[0])

-------------------
key_list = ["메보", "메인래퍼", "메보22", "사장"]
value_list = ["서다현", "코토네", "이지우", "정병기"]
tri_last = {}

for i in range(len(key_list)) :
    tri_last[key_list[i]] = value_list[i]

print(tri_last)

---------------------

quiz = (["구름이의 나이는?", "9", 2], ["구름이의 견종은?", "비숑", 3], ["구름이의 취미는?", "잠자기", 4])
answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in quiz :
    print(item[0])
    user = input()
    if user == item[1] :
        answerCount += 1
        totalScore += item[2]
    else :
        wrongAnswerCount += 1
print(f"맞춘 개수: {answerCount}")
print(f"틀린 개수: {wrongAnswerCount}")
print(f"총점: {totalScore}")

-----------------

triples_part = {"메인보컬22": "이지우", "메인래퍼": "코토네", "메인보컬": "서다현", "작곡가": "박소현", "사장": "정병기"}
user = input("멤버 조회를 원하는 파트를 말하시오. (메인보컬22, 메인래퍼, 메인보컬, 작곡가, 사장) 중에서")
print(triples_part[user])

---------------------

