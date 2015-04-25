"""
	Program that calculates the volume of a can
"""
# importing the class that contains many functions
import math

ray = float(input("Type the can's ray in inches(cm): "))
height = float(input("Type the can's height in inches(cm): "))

volume = (math.pi*(ray)**2)*height

print ("Volume =", volume,"cm3")
