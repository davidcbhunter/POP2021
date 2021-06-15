import datetime

class My_Class:
    pass

mc = My_Class()
print(id(mc))
print(id(My_Class))

print(id(str))
print(id(float))
print(id(int))
print(id(bool))
print(id(datetime.date))

s = "Kentarou Miura"
print(id(s))
