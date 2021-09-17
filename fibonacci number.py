
# ---------------------------FIBONACCI NUMBERS------------------------------------------------
# Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
#
# The desired output is like :
# fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Answer:

a,b=1,1
list_fib=[]
while a<=55:
    list_fib.append(a)
    a,b=b,a + b
print(list_fib)


# other solution---------------

# def fibonacci(min,max):
#     fibonacci = []
#     a = min
#     while a <= max:
#         fibonacci.append(a)
#         if len(fibonacci) < 2:
#             a += a
#         else:
#             a = fibonacci[-1] + fibonacci[-2]
#     return fibonacci
# print(fibonacci(1,55))



# other solution---------------
# this is How many terms fibonacci ??

# nterms=int(input("How many terms? "))
# n1, n2 = 0, 1
# count=0
# while count<nterms:
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1
# print(n1)
