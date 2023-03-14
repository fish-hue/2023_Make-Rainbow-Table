import re

# Function to replace vowels
def replace_vowels(word):
    replacements = {"a": "@", "e": "3", "i": "1", "o": "0", "s": "$"}
    for key, value in replacements.items():
        word = word.replace(key, value)
    return word

# Prompt the user for the filename and output filename
filename = input("Enter the name of the wordlist file(s), separated by commas: ")
output_filename = input("Enter the name of the output file: ")

# Prompt the user if they want to replace vowels
replace_vowels_option = input("Do you want to replace vowels? (y/n) ")
replace_vowels_flag = replace_vowels_option.lower() == "y"

# Split the input filenames by commas
filenames = filename.split(',')

# Set to keep track of all combinations
combinations = set()

# Open the output file for writing
with open(output_filename, 'w') as output_file:
    # Loop over each input file
    for filename in filenames:
        # Open the file and read the contents into a list
        with open(filename.strip()) as f:
            wordlist = f.readlines()

        # Loop over each word in the wordlist
        for word in wordlist:
            # Strip whitespace and newline characters
            word = word.strip()

            # Skip if the word contains numbers or special characters
            if re.search(r"\d|\W", word):
                continue

            # Replace vowels if the user wants to
            if replace_vowels_flag:
                word = replace_vowels(word)

            # Change the first character to uppercase
            word = word.capitalize()

            # Generate combinations of numbers and add them to the word
            for digits in range(2, 5):
                for number in range(1, 10**digits):
                    formatted_number = str(number).zfill(digits)
                    combination = f"{word}{formatted_number}"
                    if combination not in combinations:
                        combinations.add(combination)
                        output_file.write(f"{combination}\n")
                        print(f"Added combination: {combination}")
                    else:
                        print(f"Duplicate combination: {combination}")
        output_file.write("\n")
