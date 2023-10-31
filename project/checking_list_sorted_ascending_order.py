def is_sorted(lst):
    return lst == sorted(lst)

numbers = [1, 2, 3, 4, 5]
if is_sorted(numbers):
    print("The list is sorted.")
else:
    print("The list is not sorted.")

