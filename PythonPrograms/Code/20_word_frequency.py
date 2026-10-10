def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        # Strip simple punctuation
        clean_word = word.strip(".,!?;:\"'")
        if clean_word:
            freq[clean_word] = freq.get(clean_word, 0) + 1
    return freq

if __name__ == "__main__":
    sentence = input("Enter sentence: ")
    print(word_frequency(sentence))