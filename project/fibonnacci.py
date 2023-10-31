def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

num_terms = 10
result = fibonacci_sequence(num_terms)
print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]