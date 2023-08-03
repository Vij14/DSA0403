import string

def preprocess_text(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.lower()

def calculate_word_frequency(reviews_data):
    word_freq = {}
    for review in reviews_data:
        processed_review = preprocess_text(review)
        words = processed_review.split()
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq

def main():
    # Sample dataset, replace this with your actual dataset
    reviews_data = [
        "This product is amazing and worth every penny.",
        "I didn't like the quality of the product. Disappointed!",
        "The customer service was excellent, but the product was average.",
        # Add more reviews here
    ]

    word_frequency = calculate_word_frequency(reviews_data)

    # Sort the word_frequency dictionary by values (word counts) in descending order
    sorted_word_freq = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

    for word, frequency in sorted_word_freq.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
