from collections import Counter

def count_words_counter():
    input_string = input("Введите строку: ")
    words = input_string.lower().split()
    word_counts = Counter(words)
    
    for word, count in word_counts.items():
        print(f"{word.upper()}: {count}")

count_words_counter()
