def is_palindrome_number(n):
    if n < 0:
        return False
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(is_palindrome_number(num))