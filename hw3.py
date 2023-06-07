a = int(input("Your age: "))
b = int(input("Your height: "))

if a > 18:
	if b > 150:
		print("Вы можете посетить этот аттракцион")
	else:
		print("Вы не можете посетить этот аттракцион")
else:
	print("Вы не можете посетить этот аттракцион")
