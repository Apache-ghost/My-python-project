def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 3, 4, 2, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]
