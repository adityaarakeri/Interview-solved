# 0 1 8 27 64

def gen(limit):
    for i in xrange(limit):
        yield i**3

for f in gen(5): print f
