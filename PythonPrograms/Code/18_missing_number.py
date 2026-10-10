def find_missing_number(lst):
    # Expecting array from 1 to n containing n-1 numbers
    n = len(lst) + 1
    total = n * (n + 1) // 2
    return total - sum(lst)

if __name__ == "__main__":
    items = list(map(int, input("Enter numbers: ").split()))
    print(find_missing_number(items))