def find_max_min(numbers):
    if not numbers:
        return None, None  
    else:
        return max(numbers), min(numbers)

numbers_list = [5, 2, 8, 1, 6, 9, 3]
max_value, min_value = find_max_min(numbers_list)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
