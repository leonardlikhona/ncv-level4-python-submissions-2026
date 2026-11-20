marks = []
text = input("Enter a mark (0-100) or x to finish: ")
while text != "x":
    if text.isdigit() and int(text) <= 100:
        marks.append(int(text))
    
    else:
        print("invalid mark ignored.")
    text = input("Enter a mark (0-100) or x to finish: ")
                              