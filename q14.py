def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:
            break  
        lines.append(line)
    return lines

print("Enter multiple lines of input. Press Enter on an empty line to finish.")
user_lines = read_multiple_lines()
print("\nAll lines entered:")
for line in user_lines:
    print(line)
