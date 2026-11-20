# NCV Level 4 | Day 3 Collections and Records | example: dict_basics
# Type it in Thonny, run it, then change one thing.
learner = {"name": "Thandi", "mark": 65}
learner["mark"] = 70
learner["age"]= 20
learner["city"] = "Soshanguve"
 #learner["age"]
print(learner["name"], learner["mark"], len(learner))
for key in learner:
    print(key, "->", learner[key])
#print(learner.get("age", "unknown"))

# Expected output:
# Thandi 70 2
# name -> Thandi
# mark -> 70
# unknown
