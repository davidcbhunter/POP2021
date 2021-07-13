def add(a,b):
    return a + b

def square(a):
    return a * a

def half(a):
    return a/2

x = add(5,10)
print(x)

x = add(5,square(7))
print(x)

x = add(5,half(square(7)))
print(x)

x = square(half(add(50,60)))
print(x)
