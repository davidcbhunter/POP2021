import random
studentA = []

for x in range(100):
    f = int(random.gauss(30,10))
    if f > 100:
        f = 100
    if f < 0:
        f = 0
    studentA.append(f)
print(studentA)
