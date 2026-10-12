def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

if __name__ == "__main__":
    num = float(input("Enter number: "))
    print(check_number(num))




