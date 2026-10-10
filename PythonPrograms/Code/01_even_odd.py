def check_even_odd(n: int) -> str:
    """Return whether a number is Even or Odd."""
    if n % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(check_even_odd(num))