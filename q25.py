def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                
                contents = source.read()
            
                destination.write(contents)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: One of the files does not exist.")
    except IOError:
        print("Error: Unable to read or write the file.")

source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
