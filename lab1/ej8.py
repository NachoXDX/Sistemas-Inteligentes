import random
a = set()
while not len(a) == 10:
    a.add(random.randrange(0,999))
print(sorted(a)) 