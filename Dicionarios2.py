'''
Created on May 1, 2015

Este exercicio mostra de forma mais complexa o funcionamento de
dicionarios.

@author: bruno
'''

# Create a mapping of state to abreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities["NY"] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print("-"*10)
print("NY state has:",cities['NY'])
print("OR state has:",cities["OR"])

# print out some states
print('-'*10)
print("Michigan's abbreviations is:",states["Michigan"])
print("Florida's abbreviation is:",states['Florida'])

# Now a shortcut to find cities using the state'name instead of the abbreviation
print('-'*10)
print("Michigan has:",cities[states['Michigan']])
print('Florida has:',cities[states['Florida']])

# print every state abbreviation
print("-"*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-'*10)
for abbrev, city in cities.items():
    print("%s has %s" % (abbrev, city))
    
# now do both at the same time: State vs City
print("-"*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s and has %s" % (state, abbrev, cities[abbrev]))

# safly get a abbreviation by state that might not be there 
print("-"*10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# getting a city with a default value
print("-"*10) 
city = cities.get('TX','Does not exist')
print("The city for the state TX is: %s" % (city))

# the same thing above, but now with a existing state
print("-"*10) 
city = cities.get('FL','Does not exists')
print("The city for the state FL is: %s" % (city))