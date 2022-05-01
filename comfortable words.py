#  Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.
#
# A comfortable word is a word which you can type always alternating the hand you type with
# (assuming you type using a Q-keyboard and use of the ten-fingers standard).
# The word will always be a string consisting of only letters from a to z.
# Write a program which returns True if it's a comfortable word or False otherwise.
#
#  Answer:

left_letters=["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
right_letters=["y", "u", "i", "o", "p", "h", "j", "k", "l", "n","m"]
your_word=input("Please enter your word >:")
left_bool=False
right_bool=False
for i in your_word:
    if i in left_letters:
        left_bool=True
    if i in right_letters:
        right_bool = True
if right_bool==True and left_bool==True:
    print("Your word is a comfortable word.")
elif right_bool==True and left_bool==False:
    print("Your word is a right hand fingers.")
elif right_bool==False and left_bool==True:
    print("Your word is a left hand fingers.")
else:
    print("your word doesn't inclued any letters")

#----other solution----------------------------------

# left_letters={"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
# right_letters={"y", "u", "i", "o", "p", "h", "j", "k", "l", "n","m"}
# your_word=input("Please enter your word >:")
# set_word=set(your_word)
# left_bool=bool(set_word-left_letters)
# right_bool=bool(set_word-right_letters)
# result=left_bool and right_bool
# print(result)

# comfortable=True, left or right= False