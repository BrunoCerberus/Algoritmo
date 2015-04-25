"""
	A programm that calculates the consuption of gasoline
"""

average_velocity = int(input("Type your average velocity: "))
travel_time = float(input("Type your travel time: "))

# ds = v.dt
distance = average_velocity * travel_time

gasoline_used = distance / 12

# the float value here is formated like a integer value
print("Consumed %d L" % gasoline_used)
