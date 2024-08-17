from collections import Counter

def count_words_in_file(file_name):
    # Initialize a Counter to store word counts
    word_counts = Counter()

    try:
        # Open the file in read mode
        with open(file_name, 'r', encoding='utf-8') as file:
            # Read the file line by line
            for line in file:
                # Convert to lowercase and split into words
                words = line.lower().split()

                # Clean each word by removing punctuation
                cleaned_words = [''.join(char for char in word if char.isalnum()) for word in words]

                # Update the Counter with the cleaned words
                word_counts.update(cleaned_words)

        # Sort the word counts in alphabetical order
        sorted_word_counts = dict(sorted(word_counts.items()))

        # Print the word counts
        for word, count in sorted_word_counts.items():
            if word:  # Avoid counting empty strings
                print(f'{word}: {count}')

    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
