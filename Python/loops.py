# val1 = input('Enter a value: ')
# operand = input('Enter an operand(+, -, *, /)')
# val2 = input('Enter anothher value: ')
# you have to be careful when your doing things like the operand, or probbably learn the right sequence

# loops are continuous bodies of logic or blocks of logic that should repeat until thyre told to stop repeating

# if 10 > 20:
#     print('10 is greater than 20')

# elif 500 == 5000:
#     print('500 is equal to 5000')

# else:
#     print('both conditions are wrong')


# our_flag = 50 == 1000  # false without doubt

# if our_flag:  # if our_flag is what?? i.e. if 50 == 1000, understood this block
#     print('50 is equal to 5000')

# # whats false exactly?? our flag is already false from declaration, so are we saying; else if our flag is false false (i.e. true)??
# elif False:
#     print('really??')

# elif True:  # our_flag isnt true, so how come its printing this block??
#     print('running true block')

# else:
#     print('youre a crazy dude')


# while loop

# is_nighttime = True

# hour_of_the_day = 0

# while is_nighttime:
#     print('The time is %d o clock' % hour_of_the_day)

#     if hour_of_the_day == 5:
#         print('its time for fajr')

#     elif hour_of_the_day == 7:
#         print('Off to work')

#     elif hour_of_the_day == 10:
#         print('Breaktime')

#     elif hour_of_the_day == 14:
#         print('desired closing period')
#         break
#     hour_of_the_day = hour_of_the_day + 1
# print('you have the rest of the day')


# is_running = True

# print('Welcome to New CLI Calculator')

# while is_running:

#     print('Starting Calc....')

#     try:
#         val_one = float(input('Enter First Valid Number: '))
#     except:
#         print('Invalid Numbers, Try Again')
#         continue

#     operator = input(
#         'Enter your desired operator, (+, -, *, /, %): ')

#     try:
#         val_two = float(input('Enter Second Valid Number: '))
#     except:
#         print('Invalid Numbers, Try Again')
#         continue

#     if operator == '+':
#         print(val_one + val_two)

#     elif operator == '-':
#         print(val_one - val_two)

#     elif operator == '*':
#         print(val_one * val_two)

#     elif operator == '/':
#         print(val_one / val_two)

#     elif operator == '%':
#         print(val_one % val_two)

#     else:
#         print('invalid operator, Try Again!')

#     end = input('Would you like to perform another operation? [yes, no] ')
#     if end == 'yes':
#         pass

#     elif end == 'no':
#         is_running = False


# flag = i = 1
# while flag:
#     print(i)
#     i = i + 1
#     if i == 5:

#         print('the end')


# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         count += 1
#         print(x)

# print('we have %d even numbers' % count)


# conversion = True

# while conversion:

#     print('Weight Calculator')

#     try:
#         weight = float(input('enter your weight: '))
#     except:
#         print('Invalid Weight')
#         continue

#     try:
#         unit = input('Enter K for Kg(s) or L for Lb(s): ')
#     except:
#         print('Invalid Unit, Try Again..!')
#         continue

#     if unit == 'K' or 'k':
#         print(weight * 2.2)

#     elif unit == 'L' or 'l':
#         print(weight * 0.453)

#     else:
#         print('Wrong Unit Entered')

#     end = input('Do you want to get another weight? /n [Yes, or No] ')

#     if end == 'Yes':
#         continue

#     elif end == 'No':
#         break


print('weight converter')

weight = float(input('enter your Weight: '))
unit = input('enter unit[K for Kg or L for Pounds]: ')

if unit == 'k' or 'k':
    print(weight * 2.2)

elif unit == 'L' or 'l':
    print(weight / 0.4)

else:
    print('Invalid Unit')


print()
