x = 10
y = -10

# Bad
tmp = y
y = x
x = tmp

# Better
x, y = y, x





# Bad
print(int('1'))

# Better
try:
	print(int('1'))
except:
	print('Conversion failed!')
else:
	print('Conversion successful')
finally:
	print('Executes even when exception fires!')





shelters = ['Tent', 'Caravan', 'House', 'Castle']

# Bad, assumes four parameters
smallest, _, _, largest = shelters

# Better
smallest = shelters[0]
largest = shelters[-1]

# Better
smallest, *rest, largest = shelters





import string
cities = [
	'Groningen',
	'Marseille',
	'Buenos Aires',
	'Mumbai'
	]
populations = [
	197823,
	852516,
	2890151,
	12442373
	]

# Bad
d = {}
for city, population in zip(cities, populations):
	d[string.capwords(city)] = population
print(d)

# Better, dictionary comprehension
d = { string.capwords(city) : population for city, population in zip(cities, populations) }
print(d)

# Better, preserves order
import collections
d = collections.OrderedDict()
for city, population in zip(cities, populations):
	d[string.capwords(city)] = population
print(d)

