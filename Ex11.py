"""
	Program that converts meters to inches and feets
"""

def meter2inche(meter):
	inche = meter / 0.0254
	return inche

def meter2feet(meter):
	x = meter2inche(meter)
	feet = x / 12
	return feet

meter = int(input("Type here the distance in meters: "))
inche = meter2inche(meter)
feet = meter2feet(meter)

print(meter,"m in inches is",inche, "\n",meter,"m in feets is",feet)
