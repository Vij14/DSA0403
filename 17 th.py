def main():
    # Load the dataset from CSV file
    file_path = "data.csv"
    try:
        df = pd.read_csv(file_path)
        feedback_data = df["feedback"].tolist()

        # Get user input for the top N most frequent words to display
        n = int(input("Enter the number of top frequent words to display: "))

        word_frequency = calculate_word_frequency(feedback_data)

        # Sort the word_frequency dictionary by values (word counts) in descending order
        sorted_word_freq = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))

        # Display the top N most frequent words and their corresponding frequencies
        print(f"\nTop {n} most frequent words:")
        for i, (word, frequency) in enumerate(sorted_word_freq.items()):
            if i >= n:
                break
            print(f"{word}: {frequency}")

        # Plot a bar graph to visualize the top N most frequent words and their frequencies
        top_n_words = list(sorted_word_freq.keys())[:n]
        top_n_frequencies = list(sorted_word_freq.values())[:n]

        plt.bar(top_n_words, top_n_frequencies)
        plt.xlabel("Words")
        plt.ylabel("Frequencies")
        plt.title(f"Top {n} Most Frequent Words")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    main()
