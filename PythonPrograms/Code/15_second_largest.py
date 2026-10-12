def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

if __name__ == "__main__":
    items = list(map(int, input("Enter numbers: ").split()))
    print(second_largest(items))





