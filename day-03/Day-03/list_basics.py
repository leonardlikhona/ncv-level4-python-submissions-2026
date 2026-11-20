# NCV Level 4 | Day 3 Collections and Records | example: list_basics
# Type it in Thonny, run it, then change one thing.
marks = [65, 72, 48, 90, 55, 155]
#print(marks[0], marks[-1])
#print(marks[1:4])
#marks.append(92)
#marks[2] = 58

#print(marks, len(marks))
b = marks[:]
b.append(200)
print(marks,b)

# Expected output:
# 65 55
# [72, 48, 90]
# [65, 72, 58, 90, 55, 81] 6
