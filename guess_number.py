# importing the class random from python API
import random

# using the function randint() from class random
# the first and second argumments define the scope of the values
number = random.randint(1,100)

guess = 0
times = 0
while (guess != number):
	times += 1
	guess = int(input("Enter the value: "))
	if guess > number:
		print ("The true value is less than",guess)
	if guess < number:
		print ("The true value is greater than",guess)

print ("You fucking did it! The true value is", number,
	"You won with",times,"tries")
