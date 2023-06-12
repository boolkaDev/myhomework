age = int(input())
if age % 10 == 1 and x != 11 and x%100!=11:
	print("Вам",age,"год")
elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
	print("Вам",x,"года")
else:
	print("Вам",x,"лет")