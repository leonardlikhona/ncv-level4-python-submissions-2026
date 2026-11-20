with open("notes.txt", "a") as f:
    f.write("I love python\n")
with open("notes.txt") as f:
    lines = f.readlines()
    print(len(lines))
    print(lines)