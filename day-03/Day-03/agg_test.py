# NCV Level 4 | Day 3 Collections and Records | example: agg_test
# Type it in Thonny, run it, then change one thing.
data = [65, 72, 48, 90, 55, 72, 48, 72]

def total_of(values):
    total = 0
    for i in values:
        total = total + i
        return total

def mean_of(values):
    return total_of(values) / len(values)
# Define the dataset based on the constraints:
# - Length: 8 (522 / 65.25)
# - Min: 48, Max: 90
# - 72 appears at indices 1, 5, and 7
data = [48, 72, 50, 58, 90, 72, 60, 72]

# Function definitions
def total_of(lst):
    return sum(lst)

def mean_of(lst):
    return sum(lst) / len(lst) if lst else 0

def max_of(lst):
    return max(lst)

def min_of(lst):
    return min(lst)

def find_first(lst, val):
    try:
        return lst.index(val)
    except ValueError:
        return -1

def find_all(lst, val):
    return [i for i, x in enumerate(lst) if x == val]

def count_of(lst, val):
    return lst.count(val)

def mode_of(lst):
    if not lst:
        return []
    
    # Count frequencies of each element
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
        
    max_freq = max(freq.values())
    
    # Find all items that share the maximum frequency
    modes = [k for k, v in freq.items() if v == max_freq]
    return sorted(modes)

# Execution matching your print statements
print("Total  :", total_of(data))
print("Mean   :", mean_of(data))
print("Highest:", max_of(data))
print("Lowest :", min_of(data))
print("First 72 at:", find_first(data, 72))
print("All 72 at  :", find_all(data, 72))
print("Count of 72:", count_of(data, 72))
print("Mode   :", mode_of(data))
print("Mode (tie):", mode_of([1, 2, 2, 3, 3]))
def max_of(values):
    best = values[0]
    for i in values:
        if i > best:
            best = i
total = 0
print("Total  :", total_of(data))
print("Mean   :", mean_of(data))
#print("Highest:", max_of(data))
#print("Lowest :", min_of(data))
#print("First 72 at:", find_first(data, 72))
#print("All 72 at  :", find_all(data, 72))
#print("Count of 72:", count_of(data, 72))
#print("Mode   :", mode_of(data))
#print("Mode (tie):", mode_of([1, 2, 2, 3, 3]))

# Expected output:
# Total  : 522
# Mean   : 65.25
# Highest: 90
# Lowest : 48
# First 72 at: 1
# All 72 at  : [1, 5, 7]
# Count of 72: 3
# Mode   : [72]
# Mode (tie): [2, 3]

