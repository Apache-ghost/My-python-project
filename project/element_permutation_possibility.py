from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

elements = [1, 2, 3]
result = generate_permutations(elements)
print(result)  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]