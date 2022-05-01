#
# ----------------------------Front-Back Char------------------------------
#
# Given a string, return a new string where the first and last chars have been exchanged.
# For example:
#
# Test	Result
# print(front_back('a'))
# a
# print(front_back('ab'))
# ba

# Solution:----------------

def front_back(word):
    if len(word)==1:
        word=word
    elif len(word)>1:
        word=word[-1]+word[1:-1]+word[0]
    return word
print(front_back("word"))