#Mapping of state to abbreviation

states = {
'Oregon': 'OR', 
'Florida': 'FL', 
'California': 'CA', 
'New York': 'NY', 
'Michigan': 'MI'
}


#Create a basic set of states and cities
cities = {
	'CA': 'San Francisco', 
	'MI': 'Detroit', 
	'FL': 'Jacksonville'
	}

#add some more cities
cities['NY'] = 'New York'
#cities['NY'] = 'Binghamton'
cities['OR'] = 'Portland'

#print cities
print('-' * 25)
print("NY State has: ", cities['NY'])
print("CA has: ", cities['CA'])

#print out some states
print('-' * 25)
print("New York State is: ", states['New York'])
print("California is: ", states['California'])

#print cities using state and then cities dict
print('-' * 25)
print("New York has:", cities[states["New York"]])
print("California has:", cities[states["California"]])

#print every state abbreviation
print('-' * 25)
for state, abbreviation in list(states.items()):
	print(state + " is abbreviated to " + abbreviation)



#print every city in state
print('-' * 25)
for state, city in list(cities.items()):
	print(f"{state} has {city}")

#print both city and state at the same time
print('-' * 25)
for state, abbrev in list(states.items()):
	print(f"{state} has abbreviation {abbrev}")
	print(f"{abbrev} has {cities[abbrev]}")

#get abbreviation of state that may not be there in the dictionary
print('-' * 25)
state = states.get('Texas')
if not state:
	print("Texas not present in states!")

#get city with default value
print('-' * 25)
city = cities.get('TX', 'Does not exist')
print(f"The city for the state TX is: {city}")

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:

#dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#OUTPUT -> {'sape': 4139, 'guido': 4127, 'jack': 4098}

l1 = [('Vignesh', 22), ('Chethana', 25)]
print(dict(l1))

dictionary = {x: x**2 for x in (2, 4, 6)}
print(dictionary)


#When the keys are simple strings, it is sometimes easier to specify pairs 
#using keyword arguments
newdict = dict(sape=4139, guido=4127, jack=4098)
print(newdict)

#https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6
#Pertaining to Python ordering, from Python 3.6, 3.7 onwards

#OrderedDict — Remember the Order Keys are Added to a Dictionary for Python versions < 3.6

