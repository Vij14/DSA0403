import string

def process_text(text):
    # Remove punctuation and convert text to lowercase
    translator = str.maketrans('', '', string.punctuation)
    processed_text = text.translate(translator).lower()
    return processed_text

def calculate_frequency(text):
    words = text.split()
    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

def display_frequency_distribution(word_frequency):
    sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

    for word, frequency in sorted_word_frequency.items():
        print(f"{word}: {frequency}")

def main():
    # Read the text document
    with open("sample_text.txt", "r") as file:
        text = file.read()

    # Process the text
    processed_text = process_text(text)

    # Calculate the word frequency
    word_frequency = calculate_frequency(processed_text)

    # Display the frequency distribution
    print("Frequency Distribution of Words:")
    display_frequency_distribution(word_frequency)

if __name__ == "__main__":
    main()
