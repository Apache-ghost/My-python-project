def factorial(num):
    if num == 0:
        return 1
    elif  num<0:
            return " the factorial of negative numbers cannot be evaluated"
    else:
        return num * factorial(num - 1)

number = 5
result = factorial(number)
print(result)  # Output: 120
