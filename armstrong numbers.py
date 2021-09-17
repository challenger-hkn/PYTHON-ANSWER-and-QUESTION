
                        # Armstrong Number
# Find out if a given number is an "Armstrong Number".
#
# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
# 371 = 33 + 73 + 13;
# 9474 = 94 + 44 + 74 + 44;
# 93084 = 95 + 35 + 05 + 85 + 45.
#
# Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to the user.
#
# 407   	407 is an Armstrong number
# 5	    5 is an Armstrong number


# Answer:

while True:
    number = input("Enter your number (Press 'q' for excape) : ")
    if number == "q":
        break
    lenght = len(number)
    total=0
    for i in range(lenght):
        total = total + int(number[i])** lenght
    if (total == int(number)):
        print("Your number is a Armstrong Number!")
    else:
        print("Your number is not a Armstrong Number!")



#-----alternative solution---------------------------------------

# while True:
#     number=input("enter a positive digit number : ")
#     digits=len(number)
#     summ=0
#
#     if not number.isdigit():
#         print(number, "is invalid entry.Enter a valid number.!")
#     elif int(number)>=0:
#         for i in range(digits):
#             summ=summ+ int(number[i])**digits
#         if summ==int(number):
#             print(number,"is an Armstrong number.")
#             break
#         else:
#             print(number, "is not Armstrong number sorry")
#             break