
# ----------------------PARROT TROUBLE-----------------------------

#
# We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.
# Define a function taking two parameters (talking and hour) to return True if we are in trouble.
# The argument to  talking parameter can only be True or False whether it is talking or not.
# The argument to hour parameter should be the current hour time in the range of 0 to 23.
# For example:
#
# Test	Result
# print(parrot_trouble(True, 5))
# True
# print(parrot_trouble(True, 8))
# False
# print(parrot_trouble(False, 22))
# False

# Solution 1:
def parrot_trouble(talking, hour):
    hour=int(hour)
    hour= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    hour= int(list(0,1,2,3,4,5,22,23,24))
    (talking==True and "True") or (talking==False and "False")
    if (0<hour<6 and "True") and (21<hour<=23 and "True"):
    if (0<=hour<=6) or (21<hour<=23):
        hour=True
    if talking==True and hour==True:
        return True
    else:
        return False
print(parrot_trouble(False,22))


# Solution 2:--------------------

# def parrot_trouble(talking, hour):
#     hour=int(hour)
#     if (0<=hour<6) or (21<hour<=23):
#         hour=True
#     if talking==True and hour==True:
#         return True
#     else:
#         return False
#
# print(parrot_trouble(False,23))

