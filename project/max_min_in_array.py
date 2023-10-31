def find_min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return minimum, maximum

numbers = [5, 2, 8, 1, 9]
min_num, max_num = find_min_max(numbers)
print(f"Minimum: {min_num}, Maximum: {max_num}")  # Output: Minimum: 1, Maximum: 9
