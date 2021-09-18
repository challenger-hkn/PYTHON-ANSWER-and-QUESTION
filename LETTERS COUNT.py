
#-------------------LETTERS COUNT------------------------

# Count the number of each letter in a sentence.
# The department you work for undertook a project construction that makes word / text analysis.
# You are asked to calculate the number of letters or any chars in the sentences entered under this project.
#
# Write a Python program that;
# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.
#
# Examples
# Sample inputs	Outputs
# hippo runs to us!
# {'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1,
# 'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}

#Solution 1

# input=str("hippo runs to us!")
# liste={}
# for i in input:
#     keys = liste.keys()
#     if i in keys:
#         liste[i] += 1
#     else:
#         liste[i] = 1
# print(liste)


# solution 2
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))

# solution 3
#
# input=str("hippo runs to us!")
# input=list(input)
# inputs=set(input)
# liste2={}
# for i in inputs:
#     k=input.count(i)
#     liste1=dict.fromkeys(i,k)
#     liste2.update(liste1)
# print(liste2)


# solution 4-----------------
# def counter(word):
#     from collections import Counter
#     return Counter(word)
# print(counter("This is nice job"))

# solution 5-----------------
# word="Hello"
# letter={}
# for i in word:
#     if i in letter:
#         letter[i] += 1
#     else:
#         letter[i] =  1
# print(letter)


# solution 6-----------------
# input=str("hippo runs to us!")
# input=list(input)
# inputs=set(input)
# value=[]
# key=[]
# for i in inputs:
#     k=input.count(i)
#     value.append(k)
#     value.append(k)
#     key.append(i)
#
# print(*zip(inputs,value))

