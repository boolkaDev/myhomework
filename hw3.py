a = int(input("Your age: "))
b = int(input("Your height: "))

if a > 18:
	if b > 150:
		print("Вы можете посетить этот аттракцион")
	if b <= 150:
		print("Вы не можете посетить этот аттракцион")
if a <= 18:
	print("Вы не можете посетить этот аттракцион")
