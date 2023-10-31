def sum_even_numbers():
    total = 0
    for num in range(1, 101):
        if num % 2 == 0:
            total += num
    return total

result = sum_even_numbers()
print(result)  # Output: 2550

