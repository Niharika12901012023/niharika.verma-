def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers_list = [1, 2, 3, 4, 5]
sum_of_numbers = calculate_sum(numbers_list)
print("Sum of numbers:", sum_of_numbers)
