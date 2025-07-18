def frequency_of_words(word_list):
    unique_words = set(word_list)
    counts = {word: 0 for word in unique_words}
    for i in unique_words:
        for j in words:
            if i == j:
                counts[i] += 1
    return counts

words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
print(frequency_of_words(words))