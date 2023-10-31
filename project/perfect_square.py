def is_perfect_square(num):
    return num ** 0.5 == int(num ** 0.5)

number = 16
if is_perfect_square(number):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")