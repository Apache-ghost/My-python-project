def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 24
num2 = 36
result = gcd(num1, num2)
print(result)  # Output: 12