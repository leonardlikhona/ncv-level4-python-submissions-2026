name = " Thandi Mokoena "
print(len(name))
print(len(name.strip()))
print(name.strip().upper())
      
with open("log.txt", "w") as f:
     f.write("first\n")
with open("log.txt", "w") as f:
      f.write("second\n")
with open("log.txt") as f:
      print(f.read())
