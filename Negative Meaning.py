

# ---------------------Negative Meaning--------------------------------------------

# Define a function to take a word and return negative meaning.
# Given a word, return a new word where "not " has been added to the front.
# However, if the word already begins with "not", return the string unchanged.
#
# For example:
#
# Test	Result
# print(not_string('sugar'))
# not sugar
# print(not_string('x'))
# not x
# print(not_string('not bad'))
# not bad

# Solution :
def not_string(word):
    new_word=word.split()
    for i in new_word:
        if i!="not":
            word = "not"+" "+ word
            return word
        else:
            return word
print(not_string("not aplle"))