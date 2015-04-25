"""
	An Algorithm that reads two numbers and prompts the sum
"""

num1 = int(input("Type a number: "))
num2 = int(input("Type a second number: "))

# I can do in this way
print ("The sum is",num1+num2)

# Or
print ("The sum is %d" % (num1+num2))

# Or Or
# sum_number = num1 + num2
# print ("The sum is " + sum_number)
# But i can't use to the concatenator "+", because this thing tries to
# convert a int object to a str object, and that is not possible in this way
