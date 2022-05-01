
                    #-------------PRIME NUMBERS------------

# Write a program that takes a number from the user and prints the result to check if it is a prime number.
#
# The examples of the desired output are as follows :
#
# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number


# Answer:

n=int(input("enter a positive number>:"))
count=0
for i in range(1,n+1):
    if n% i==0:
        count +=1
if (n==0) or (n==1) or (count>=3):
    print(n,"is not a prime Number.")
else:
    print(n,"is a prime number")


# -----------------------PRIME NUMBERS - limit n------------------------
#  Print the prime numbers which are between 1 to entered limit number (n).
#
# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :
#
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]


# Answer:

# liste1 = []
# for i in range(2, 101):
#   for j in range(2,i):
#     if i%j == 0:
#       break
#   else:
#     liste1.append(i)
# print(liste1)
