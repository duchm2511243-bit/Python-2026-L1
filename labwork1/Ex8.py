def extract_even(values):
    return [num for num in values if num % 2 == 0]


sample_list = [1, 4, 5, -1, 10]
result = extract_even(sample_list)

print("Original list:", sample_list)
print("Even numbers:", result)