import random

def bubble_sort(values):
    items = list(values)
    n = len(items)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1
    return comparisons, swaps

def selection_counts(values):
    val = list(values)
    n = len(val)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if val[j] < val[min_idx]:
                min_idx = j
        val[i], val[min_idx] = val[min_idx], val[i]
        swaps += 1
    return comparisons, swaps

random.seed(7)
for n in (8, 20, 100):
    values = [random.randint(0, 100) for m in range(n)]
    print(n, "bubble", bubble_sort(values), "selection", selection_counts(values))
