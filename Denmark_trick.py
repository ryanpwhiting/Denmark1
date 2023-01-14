
from data import animal_list
from data import color_list

# First Question

num = int(input('Hello, please choose a number between 1 and 10\n'))

while num not in range(1, 11):
    num = int(input("I'm sorry, that's not an acceptable answer! Please choose an integer between 1 and 10.\n"))

# Second Question
magic_num = (num) * 9

print('Now multiply that number by 9')

while int(input()) != magic_num:
    print("I'm sorry, that's not correct!")

# Third Question
sum = 0
for digit in str(magic_num):
    sum += int(digit)

print('Now add the two digits together (if you chose 1 add 0 + 9)')

while int(input()) != sum:
    print("I'm sorry, that's not correct!")

# Fourth Question

print('Now subtract that number by 5')

easy_num = sum - 5

while int(input()) != easy_num:
    print("I'm sorry, that's not correct!")

# Fifth Question

dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}

magic_letter = dict.get(easy_num)

real_letter = input('Now find the coresponding letter to your number. For example 1 = A, 2 = B, 3 = C, 4 = D, 5 = E, 6 = F \n')


while real_letter.lower() != magic_letter.lower():
    real_letter = input("Is that the right letter?\n")

# Sixth Question

count_list = ['denmark', 'djibouti', 'democratic republic of the congo', 'drc', 'dominica', 'dominican republic',]

my_country = input('Now choose a country that starts with the letter you now have. \n')


while my_country.lower() not in count_list:
    my_country = input("I don't think that's a countrie that starts with your letter!\n")

prefered_answer = 'Denmark'

while my_country.lower() != prefered_answer.lower():
    my_country = input("That is a country that starts with D but for this game please choose one that's further north!\n")

# Seventh Question



their_animal = input('Now choose an animal that starts with the same letter that your country ended with.\n')

while their_animal.lower() not in animal_list:
    their_animal = input('Is that right?\n')


while their_animal.lower() != animal_list[0]:
    their_animal = input("You've got the right letter just the wrong animal. Try again!\n")

# Eigth Question

their_color = input('Now choose a color that starts with the same letter that your animal ended with.\n')

while their_color.lower() not in color_list:
    their_color = input("I've never heard of that color! Try again!\n")


while their_color.lower() != color_list[0]:
    their_color = input("You're on the right track, but choose a more common option!\n")

# Ninth Question

print('Did you get an Orange Kangaroo from Denmark?!')















