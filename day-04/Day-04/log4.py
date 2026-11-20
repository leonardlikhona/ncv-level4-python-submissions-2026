f = open("notes.txt", "a")

f.write("Hello Humbulani\n")
f.write("Second line\n")
#f.write("I love Python \n")
f.close()
print("saved")
f = open("notes.txt", "r")
print(f.read())