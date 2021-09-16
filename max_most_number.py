# Task : Find out the most frequent number and its frequency.
#
# Write a program that;
#
# Finds out the most frequent number in the given list.
# Calculates its frequency.
# Prints out the result such as :
#
# Given list	Desired Output
# numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
# the most frequent number is 3 and it was 4 times repeated


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_common = max(list(numbers), key=numbers.count)
iteration = numbers.count(most_common)
print("The most frequent numbers is {} and it was {} times repeated iteration".format(most_common, iteration))
