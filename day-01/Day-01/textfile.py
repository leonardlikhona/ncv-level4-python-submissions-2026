def is_competent(mark, pass_mark=50):
    return mark >= pass_mark 
print(is_competent(65))
print(is_competent(45))
print(is_competent(45, 40))
print(is_competent(mark=45, pass_mark=40))
