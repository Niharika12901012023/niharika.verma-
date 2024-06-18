def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


filename = input("Enter the name of the file to read: ")


read_file(filename)
