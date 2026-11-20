learners = {}

def add_learners(learners, number, name):
    if number in learners:
        return False
    learners[number] = {"name": name, "marks": [1]}
    return True

def add_mark(learners, number, mark):
    if number not in learners:
        return False
    learners[number]["mark"].append(mark)
    return True

def rename_learner(learners, number, new_name):
    if number not in learners:
        return False
    learners[number]["name"] = new_name
    return True

learners = {}
print(add_learners(learners, "2024001", "Thandi"))
print (add_learners(learners, "2024001", "Sipho"))
print(add_mark(learners, "2024001", 65))
print(add_mark(learners, "2024001",72))
print(add_mark(learners, "9999999", 50))
print(rename_learner(learners, "2024001","Thandi M"))
print(learners)
print(learners)