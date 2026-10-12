def find_largest(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    a, b, c = map(int, input("Enter 3 numbers: ").split())
    print("Largest:", find_largest(a, b, c))




