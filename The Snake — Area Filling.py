# https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt
#
# --------------------The Snake — Area Filling----------------

# This challenge is based on the classic videogame "Snake".
# Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.
#
# For example, if n = 7 the game looks something like this:
# In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).
# Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.
#
# Examples
# snakefill(3) ➞ 3
# snakefill(6) ➞ 5
# snakefill(24) ➞ 9


def addition(num):
	count = 0
	size = 1
	while size <= (num ** 2)/2:
		count += 1
		size *= 2
	return count
print(addition(6))

#alternatif solution from others--------------
# def snakefill(n):
# 	area = n**2
# 	count = 0
# 	while 2**count <= area:
# 		count += 1
# 	return count-1
# print(snakefill(24))

#alternatif solution from others-----
# import math
# def snakefill(n):
# 	return math.floor(math.log2(n**

