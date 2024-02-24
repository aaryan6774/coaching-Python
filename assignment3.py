import random as r
print(float(random.randrange(45, 95)))
print(random.randrange(450, 900, 3))

import random as r
for i in range(0, 2):
    print(random.randint(450, 950))

for i in range(0, 3):
    print(random.randrange(10, 70, 13))

for i in range(0, 3):
    print(random.randrange(10, 20, 2))

a = random.randrange(10, 20, 2)
print(a)
b = random.randrange(10, 20, 2)
c = random.randrange(10, 20, 2)
d = random.randrange(10, 20, 2)
e = random.randrange(10, 20, 2)
f = random.randrange(10, 20, 2)

mean = (a+b+c+d+e+f)/100
print(mean)
