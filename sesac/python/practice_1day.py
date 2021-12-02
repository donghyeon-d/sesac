# # 사용자 입력

# x = input("입력해주세요 : ")
# print(x)

# print('1 + 1 = ', 1 + 1)
# print("1 - 2 = ", 1 - 2)
# print("5 * 3 = ", 5 * 3)
# print("5 / 2 = ", 5 / 2)
# print("5 // 2 = ", 5 // 2)
# print("9 % 2 = ", 9 % 2)
# print("2 ** 3 = ", 2 ** 3)

# print(2 + 3 * 2)
# print((2 + 3) * 2)

# 정수 int 100, -200
# 실수 float 3.14
# 참/거짓 bool True, False
# 문자열 str "최동현"

# int 가 float보다 메모리가 작음

# print(int(5/2))

# x = input(20)
# print(x * x * 3.1415926535)

# pi = 3.1415926535
# r = input("변수명 : ")
# print(int(r) * int(r) * pi)

# #4장 변수 실습1
# x, y = 20, 30
# c = x + y
# print(c)

# a = 10
# a = a + 10
# print(a)

# print(5 > 10 and 20 == 20)
# print(5 > 10 & 20 == 20)
# print(5 > 10 or 20 == 20)
# print(5 > 10 | 20 == 20)

# print("안녕, 친구야")
# print('안녕, \n친구야')
# print("""안녕,
# 친구야""")

# print("-"*30)

# name = input("너의 이름이 뭐야?")
# print(f'내 이름은 {name}야!!!')

# 5장 Boolean과 비교, 논리연산자
# a, b, c = 20, 70, 80
# print(a > 65 and b > 70 and c > 80)

# d, e, f = 70, 80, 90
# print(d > 65 and e > 65 and f > 65)

# num_first = input("첫번째 점수: ")
# num_second = input("두번째 점수: ")
# num_third = input("세번째 점수: ")

# result = int(num_first) > 65 an70
# int(num_second) > 65 and int(num_third) > 65
# print(f"결과 : {result}")

# word = "apple banana"
# print(len(word))
# word = word.replace("apple", "orange")
# print(word)

# word = word.upper()
# print(word)

# word = word.lower()
# print(word)

text = input("아무 문자나 입력해주세요 : ")
print(text.replace(" ", ""))
