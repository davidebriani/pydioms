# Bad
twitter_search('@obama', False, 20, True)

# Better, with keyword arguments
twitter_search('@obama', retweets=False, numtweets=20, popular=True)





# Bad
doctest.testmod()
# returns (0, 4)

# Better
doctest.testmod()
# returns TestResults(failed=0, attempted=4)
# where   TestResults = namedTuple('TestResults', ['failed', 'attempted'])





# Bad, mixes business/administrative logic and is not reusable
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# Better
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()





# Bad
f = open('data.txt')
try:
	data = f.read()
finally:
	f.close()

# Better, context automatically deals with file closing
with open('data.txt') as f:
	data = f.read()





# Bad
old_context = getcontext().copy()
getcontext().prec = 50
print Decimal(355) / Decimal(113)
setcontext(old_context)

# Better
with localcontext(Context(prec=50)):
	print Decimal(355) / Decimal(113)





#
