val_one = input('Enter a number: ')
operand = input('Enter operand(+, -, *, /, %) ')
val_two = input('Enter a number: ')

add = float(val_one) + float(val_two)
subtract = float(val_one) - float(val_two)
multiply = float(val_one) * float(val_two)
divide = float(val_one) / float(val_two)
modulo = float(val_one) % float(val_two)

if operand == '+':
    print(add)

elif operand == '-':
    print(subtract)

elif operand == '*':
    print(multiply)

elif operand == '/':
    print(divide)

elif operand == '%':
    print(modulo)
