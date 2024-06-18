def write_to_file(text):
    with open("user_input.txt", "w") as file:
        file.write(text)
    print("Text successfully written to file.")


user_input = input("Enter text to write to file: ")


write_to_file(user_input)
