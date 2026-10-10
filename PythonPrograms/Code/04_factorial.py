def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("Factorial:", factorial(num))