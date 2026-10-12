def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

if __name__ == "__main__":
    text = input("Enter string: ")
    v, c = count_vowels_consonants(text)
    print(f"Vowels: {v}, Consonants: {c}")


