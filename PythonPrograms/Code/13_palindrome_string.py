def is_palindrome_string(s):
    clean = "".join(ch.lower() for ch in s if ch.isalnum())
    return clean == clean[::-1]

if __name__ == "__main__":
    text = input("Enter string: ")
    print(is_palindrome_string(text))