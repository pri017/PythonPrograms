def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    text = input("Enter string: ")
    print(char_frequency(text))