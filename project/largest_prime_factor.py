def largest_prime_factor(number):
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

num = 84
result = largest_prime_factor(num)
print(result)  # Output: 7