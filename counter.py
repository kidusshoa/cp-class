from collections import Counter

def most_frequent_words(text, n=2):
    
    words = text.lower().split()
    word_count = Counter(words)
    most_common = word_count.most_common(n)
    return dict(most_common)

text = "apple banana apple orange banana apple mango orange apple banana orange"
top_words = most_frequent_words(text)

print(top_words)