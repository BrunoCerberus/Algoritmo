#!/us/bin/env
"""
	Algorithm that reads a name and the salary, then prints how much minimun salary that person receives
"""

name = input("Type your complete name here: ")
salary = float(input("How much do you make per month: "))
minimun_salary = 700

print (name,"receives %d minimun salary" % (salary / minimun_salary))
