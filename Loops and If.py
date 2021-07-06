my_list = [56,37,82,2340,5]

largest = my_list[0]
for x in my_list:
    if x > largest:
        largest = x
        print(largest)
print(largest)


smallest = my_list[0]
for x in my_list:
    if x < smallest:
        smallest = x
        print(smallest)
print(smallest)
