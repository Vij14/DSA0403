def calculate_likes_frequency(posts_data):
    likes_freq = {}
    for post in posts_data:
        likes_count = post["likes"]
        if likes_count in likes_freq:
            likes_freq[likes_count] += 1
        else:
            likes_freq[likes_count] = 1
    return likes_freq

def main():
    # Sample dataset, replace this with your actual dataset
    posts_data = [
        {"post_id": 1, "likes": 100},
        {"post_id": 2, "likes": 50},
        {"post_id": 3, "likes": 200},
        {"post_id": 4, "likes": 100},
        # Add more posts here
    ]

    likes_frequency = calculate_likes_frequency(posts_data)

    # Sort the likes_frequency dictionary by keys (likes count)
    sorted_likes_freq = dict(sorted(likes_frequency.items()))

    for likes_count, frequency in sorted_likes_freq.items():
        print(f"{likes_count} likes: {frequency} posts")

if __name__ == "__main__":
    main()
