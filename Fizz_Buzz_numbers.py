


#---------------Fizz Buzz numbers----------------------------------------


# Task : Print the Fizz Buzz numbers.
#
# Fizz Buzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
# Print numbers from 1 to 100 inclusively following these instructions:
# if a number is multiple of 3, print "Fizz" instead of this number,
# if a number is multiple of 5, print "Buzz" instead of this number,
# for numbers that are multiples of both 3 and 5, print "FizzBuzz",
# print the rest of the numbers unchanged.
# Output each value on a separate line.
# Note that : This question is famous on the web, so to get more benefit from this assignment, try to complete this task on your own.


# Alternative 1:
# list, append

numbers = list(range(1, 101))
fizbuzz=[]
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        fizbuzz.append("FizzBuzz")
    elif i % 3 == 0:
        fizbuzz.append("Fizz")
    elif i % 5 == 0:
        fizbuzz.append("Buzz")
    else:
        fizbuzz.append(i)
print(fizbuzz)


# Alternative 2:--------------------

numbers=list(range(1,101))
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        i="FizzBuzz"
    elif i % 3 == 0:
        i="Fizz"
    elif i % 5 == 0:
        i="Buzz"
    else:
        i=(i)
    print(i)


# Alternative 3:------------------------------
# if we take a input a user,

# def fizzBuzz(n):
#     numbers = []
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             numbers.append("FizzBuzz")
#         elif i %3==0:
#             numbers.append("Fizz")
#         elif i%5==0:
#             numbers.append("Buzz")
#         else:
#             numbers.append(i)  # optionally str(i)
#     return numbers
#
# print(fizzBuzz(50))

