# a = [1, 2, 3, 4, 5, 6, 7]
# b = [1, 2, "apple", 3.14, False, "lalala", 'last']

# # a = range(10)
# # print(list(a))

# # print(b[1], b[-1])

# # print(b[0:-1], b[5:])

# a.append(8)
# print(a)

# b.remove(False)
# print(b)

# print(b.index(True))

#리스트 실습1
# x = int(input("입력해주세요"))
# a = list(range(2, x+1, 2))
# a.append(x)
# print(a)

#리스트 실습2
# a = "951110-2063423"

# b = 1900
# c = a[:2]
# birth = b + int(c)
# age = 2021 - birth +1
# print(age)


# score = {"name" : "Tom", "math" : 70, "eng" : 80}
# print(score)
# score2 = dict(name = "Tom", math = 80, eng = 70)
# print(score2)

# nameInput = input("이름을 입력해주세요 : ")
# ageInput = input("나이를 입력해주세요 : ")
# callInput = input("연락처를 입력해주세요 : ")
# nameCard = dict(이름 = nameInput, 나이 = ageInput, 연락처 = callInput)
# print(nameCard)

# nameInput2 = input("이름을 입력해주세요 : ")
# ageInput2 = input("나이를 입력해주세요 : ")
# callInput2 = input("연락처를 입력해주세요 : ")
# nameCard2 = dict(이름 = nameInput2, 나이 = ageInput2, 연락처 = callInput2)
# print(nameCard2)

# list = [nameCard, nameCard2]

# print(list)

# print(2 + 2 + 3)

score_fir = int(input("첫번째 점수를 입력해주세요 : "))
score_sec = int(input("두번째 점수를 입력해주세요 : "))
score_thir = int(input("세번째 점수를 입력해주세요 : "))

if score_fir > 100 or score_sec > 100 or score_thir > 100:
    print("잘못된 점수가 입력되었습니다")
elif score_fir > 65 and score_sec > 65 and score_thir > 65:
    print("합격")
elif score_fir >= 0 and score_sec >= 0 and score_thir >= 0:
    print("불합격")
else:
    print("잘못된 점수가 입력되었습니다")


fruit = ['사과', '오렌지']
vegetable = ['당근', '호박']

category = input("등록할 카테고리를 선택해주세요 : ")
if category == "채소":
    vegetable_input = input("등록할 채소를 입력해주세요")
    if vegetable_input == "당근" or vegetable_input == "호박":
        print("이미 등록된 채소입니다.")
    else:
        category.append(vegetable)
elif category == "과일":
    fruit_input = input("등록할 과일를 입력해주세요")
    if fruit_input == "사과" or fruit_input == "오렌지":
        print("이미 등록된 과일입니다.")
    else:
        category.append(fruit)
else:
    print("존재하지 않는 카테고리입니다")
