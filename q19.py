import string

def remove_punctuation(input_string):
    translation_table = str.maketrans("", "", string.punctuation)

    return input_string.translate(translation_table)

input_string = "Hello, World! This is an example string."
result_string = remove_punctuation(input_string)
print("Original string:", input_string)
print("String with punctuation removed:", result_string)
import string

