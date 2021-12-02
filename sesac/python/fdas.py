# # text = input("아무 문자나 입력해주세요 : ")
# # print(text.replace(" ", ""))

# name = input("이름을 입력해 주세요 : ")
# num_first = input("첫번째 점수를 입력해 주세요 : ")
# num_second = input("두번째 점수를 입력해 주세요 : ")
# num_third = input("세번째 점수를 입력해 주세요 : ")

# sum = int(num_first) + int(num_second) + int(num_third)
# print(f"저의 이름은 {name}이고 총점은 {sum}입니다.")

# kor, eng, math = 80, 75, 80
# av = (int(kor) + int(eng) + int(math))/3
# print(av)

# x = 13
# print(x % 2 == 0)


id_number = "881120-1068234"
year = str(19) + str(id_number[:2])
month = id_number[2:4]
day = id_number[4:6]

print(year)
print(month)
print(day)

if id_number[7] == '1':
    print('남자')
elif id_number[7] == '2':
    print('여자')
else:
    print('주민번호를 확인해주세요.')
