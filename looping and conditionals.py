cities = ['Marseille', 'Amsterdam', 'New York', 'London']

# Bad
i = 0
for city in cities:
	print(i, city)
	i += 1

# Better
for i, city in enumerate(cities):
	print(i, city)





x_list = [1,2,3]
y_list = [2,4,6]

# Bad
for i in range(len(x_list)):
	x = x_list[i]
	y = y_list[i]
	print(x, y)

# Better
for x, y in zip(x_list, y_list):
	print(x, y)





target = 'd'
stack = ['a', 'b', 'c']

# Bad
found = False
for letter in stack:
	if target == letter:
		print('Found!')
		found = True
		break
if not found:
	print('Not found!')

# Better, for/else instead of for-if/if not
for letter in stack:
	if target == letter:
		print('Found!')
		break
else:
	print('Not found!')

# Better, no for loop
print('Found!' if target in stack else 'Not found!')





latest_python = (3,6,0)
my_python = (3,6,0)

# Bad
msg = 'Up to date'
for i in range(len(latest_python)):
	if latest_python[i] > my_python[i]:
		msg = 'Update available'
		break
print('Update check: %s' % msg)

# Better, we're still in the case of for/else instead of for-if/if not
for latest_subversion, my_subversion in zip(latest_python, my_python):
	if latest_subversion > my_subversion:
		msg = 'Update available'
		break
else:
	msg = 'Up to date'
print('Update check: %s' % msg)

# Better, no for loop
msg = 'Update available' if latest_python > my_python else 'Up to date'
print('Update check: %s' % msg)





colors = ['red', 'green', 'blue', 'yellow']

# Bad
for i in range(len(colors) -1, -1, -1):
	print colors[i]

# Better
for color in sorted(colors, reverse=True):
	print color

# Better
for color in reversed(colors):
	print color





d = { 'Matthew': 'Blue', 'Rachel': 'Green', 'Raymond': 'Red' }

# Bad
for k in d:
	print(k, d[k])

# Better
for k, v in d.items():
	print(k, v)

# Error, can't change size of iterable during iteration
for k in d.keys():
	if k.startswith('R'):
		del d[k]

# Better
d = { k : d[k] for k in d if not k.startswith('R') }



