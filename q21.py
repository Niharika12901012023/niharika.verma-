def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 4, 4, 5, 4]
element_to_count = 4
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")
