# file_manager.py
# This program reads a text file, counts the words, and saves the result

def read_file(filepath):
    # Try to open and read the file
    try:
        file = open(filepath, "r")
        text = file.read()
        file.close()
        return text
    except FileNotFoundError:
        print("Error: the file", filepath, "was not found.")
        return None


def count_words(text):
    # Split the text into a list of words and count them
    words = text.split()
    number_of_words = len(words)
    return number_of_words


def write_results(filepath, word_count):
    # Write the word count into a new file
    file = open(filepath, "w")
    file.write("Word count: " + str(word_count))
    file.close()
    print("Results saved to", filepath)


# Main part of the program
input_file = "sample.txt"
output_file = "results.txt"

text = read_file(input_file)

if text is not None:
    total_words = count_words(text)
    print("The file has", total_words, "words.")
    write_results(output_file, total_words)
else:
    print("Could not read the file. Make sure sample.txt exists.")