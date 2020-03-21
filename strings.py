names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# Bad, concatenating needs quadratic times
s = names[0]
for name in names[1:]:
    s += ', ' + name
print s

# Better
print ', '.join(names)


