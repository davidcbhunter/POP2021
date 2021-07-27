studentA = [36, 50, 58, 59, 70, 49, 50, 58, 59, 42, 63, 43, 47, 41, \
            36, 46, 54, 78, 51, 46, 42, 41, 48, 39, 60, 47, 59, 55, \
            37, 71, 59, 37, 61, 68, 63, 45, 57, 53, 57, 40, 75, 38, \
            59, 57, 44, 30, 52, 54, 37, 63, 41, 70, 56, 46, 70, 63, \
            66, 63, 39, 61, 47, 41, 63, 43, 36, 62, 43, 44, 52, 51, \
            50, 54, 42, 38, 45, 43, 57, 68, 49, 51, 27, 48, 51, 40, \
            41, 54, 30, 42, 66, 42, 80, 46, 57, 77, 57, 64, 26, 46, 55, 43]

studentB = [93, 100, 86, 91, 100, 97, 100, 68, 98, 99, 86, 79, 87, 92, \
            91, 92, 87, 97, 93, 94, 93, 77, 93, 91, 76, 79, 86, 100, 91,\
            83, 83, 93, 79, 97, 97, 92, 100, 77, 74, 86, 96, 100, 78, 73,\
            84, 100, 84, 100, 85, 91, 88, 73, 78, 100, 100, 81, 89, 71, \
            81, 100, 81, 93, 100, 75, 100, 91, 88, 100, 100, 86, 84, 81, \
            97, 96, 88, 100, 84, 87, 82, 94, 82, 71, 82, 86, 85, 75, 100, \
            98, 95, 100, 91, 84, 76, 83, 93, 75, 78, 77, 76, 95]

studentC = [82, 85, 57, 74, 80, 66, 66, 80, 68, 75, 71, 97, 77, 98, 83, \
            85, 80, 75, 87, 81, 84, 70, 65, 95, 76, 73, 87, 72, 70, 83, \
            84, 75, 80, 93, 74, 66, 61, 74, 72, 64, 79, 92, 79, 72, 74, \
            81, 90, 89, 74, 49, 84, 95, 81, 75, 78, 69, 81, 68, 64, 75, \
            83, 78, 93, 100, 53, 75, 64, 90, 86, 84, 92, 84, 86, 95, 100,\
            72, 73, 82, 79, 66, 87, 75, 90, 91, 77, 82, 77, 61, 87, 84, \
            83, 81, 83, 71, 74, 95, 81, 94, 78, 69]

studentD = [43, 68, 59, 61, 62, 58, 80, 50, 51, 71, 56, 50, 69, 59, 63, \
            53, 57, 73, 58, 67, 72, 68, 52, 39, 66, 68, 65, 63, 52, 52, \
            59, 68, 59, 62, 59, 68, 46, 75, 64, 49, 67, 52, 59, 60, 61, \
            58, 43, 57, 70, 68, 73, 65, 48, 58, 51, 71, 47, 55, 69, 57, \
            61, 60, 57, 69, 58, 54, 56, 64, 44, 51, 75, 49, 47, 68, 57, \
            58, 60, 42, 63, 43, 58, 46, 49, 56, 53, 62, 63, 41, 70, 67, \
            65, 52, 45, 53, 70, 69, 56, 67, 48, 63]

studentE = [27, 31, 39, 46, 25, 42, 9, 7, 25, 18, 40, 47, 27, 44, 28, 26,\
            45, 32, 20, 17, 41, 24, 10, 25, 50, 49, 18, 23, 40, 37, 27, \
            23, 33, 23, 31, 36, 18, 31, 22, 34, 32, 34, 42, 33, 37, 21, \
            28, 28, 33, 25, 43, 34, 36, 41, 31, 44, 46, 29, 14, 16, 35, \
            5, 46, 24, 14, 49, 13, 33, 26, 29, 38, 25, 25, 16, 31, 18, \
            43, 30, 31, 38, 31, 17, 26, 39, 29, 20, 36, 32, 10, 20, 12, \
            18, 44, 29, 35, 29, 35, 52, 39, 26]

#find total for studentA
totalA = 0
lowestA = studentA[0]
highestA = studentA[0]
for score in studentA:
    totalA += score
    if score < lowestA:
        lowestA = score
    if score > highestA:
        highestA = score
print(totalA)
print(highestA)

#find total for studentB
totalB = 0
for score in studentB:
    totalB += score
print(totalB)

#find total for studentC
totalC = 0
for score in studentC:
    totalC += score
print(totalC)

#find total for studentD
totalD = 0
for score in studentD:
    totalD += score
print(totalD)

#find total for studentE
totalE = 0
for score in studentE:
    totalE += score
print(totalE)

#average for studentA
print(totalA/len(studentA))

print(totalB/len(studentB))

print(totalC/len(studentC))

print(totalD/len(studentD))

print(totalE/len(studentE))

#find the totals, highest, and lowest in two loops
student_list = [studentA,studentB,studentC,studentD,studentE]
totals_list = []
averages_list = []
highscore_list = []
lowscore_list = []

for student in student_list:
    total = 0
    for score in student:
        total += score
    totals_list.append(total)
print(totals_list)
