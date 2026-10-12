def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print(sum_of_digits(num))




