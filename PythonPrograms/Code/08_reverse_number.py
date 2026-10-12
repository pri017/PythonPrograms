def reverse_number(n):
    sign = -1 if n < 0 else 1
    rev = int(str(abs(n))[::-1])
    return sign * rev

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(reverse_number(num))





