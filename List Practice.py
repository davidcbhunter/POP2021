# let's make a list of school types

education = ["Nursery School", "Elementary School",\
             "Junior High School", "High School", \
             "Vocational School",\
             "College/University", "Graduate School"]

# vacation -> yasumi
# vocation -> job, work

# let's check the length of the list
#print(len(education))

# let's check how to access an item of the list
# print 3rd school
#print(education[2])


# check the beginning and ending

#print(education[0])
#print(education[6])
#print(education[len(education)-1])

# 3rd way
#print(education[-1])

# let's check negative numbers
#print(education[-7])
#print(education[-8])


# let's loop through the list
# print each school, one at a time

#for x in education:
#    print(x)

#for x in range(len(education)):
#    print(education[x])


# let's set and change the current
# level of education
current_education = 6
print(education[current_education])

if current_education + 1 < len(education):
    current_education = current_education + 1

# why bad?????
#if current_education + 1 <= len(education):
#    current_education = current_education + 1

# why OK????    
#if current_education + 1 >= len(education):
#    return

print(education[current_education])





