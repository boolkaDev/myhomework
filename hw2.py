number = int(input())
uno_reverso = 0

if number < 0: # chtoby negative cyphri pysat s pomoshu modulya
    sign = -1
    number *= -1
else: # esli ne negative
    sign = 1


while number != 0:
    digit = number % 10 # naity posledny digit
    uno_reverso = uno_reverso * 10 + digit # 
    number = (number - digit) // 10 # minus last number

uno_reverso *= sign
print(uno_reverso)
