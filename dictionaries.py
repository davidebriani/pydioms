ages = {
	'Mary': 31,
	'Jonathan': 28,
	'Dick': 51
	}

# Bad
if 'Dick' in ages:
	age = ages['Dick']
else:
	age = 'Unknown'

# Better, specifies parameter to default to
age = ages.get('Dick', 'Unknown')





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





import collections

butterfly_observations = {
	'Brown Clipper': 2,
	'Common Mormon': 11,
	'Giant Atlas Moth': 1,
	'Blue Peacock': 3
	}

# Bad
if 'Palmfly' in butterfly_observations:
	palmfly_observations = butterfly_observations['Palmfly']
else:
	palmfly_observations = 0

# Better, specifies default value in case of misses
palmfly_observations = butterfly_observations.get('Palmfly', 0)

# Better, a proper dictionary structure with a default action in case of misses
d = collections.defaultdict(lambda: 0)
d.update(butterfly_observations)
palmfly_observations = d['Palmfly']

# Even better in this scenario where the dictionary stores quantitative values
butterfly_counter = collections.Counter(butterfly_observations)
palmfly_observations = butterfly_counter['Palmfly']





colors = [ 'Red', 'Green', 'Red', 'Blue', 'Green', 'Red' ]

# Ok
d = {}
for color in colors:
	if color not in d:
		d[color] = 0
	d[color] += 1

# Better
d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1

# Better
import collections
d = collections.defaultdict(int)
for color in colors:
	d[color] += 1





names = [ 'Raymond', 'Rachel', 'Matthew', 'Roger', 'Betty', 'Melissa', 'Judith', 'Charlie' ]

# Bad
d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)

# Better
import collections
d = collections.defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)

