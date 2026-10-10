def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

if __name__ == "__main__":
    text = input("Enter string: ")
    print(reverse_string(text))