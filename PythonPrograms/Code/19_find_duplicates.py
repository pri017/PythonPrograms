def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return sorted(list(duplicates))

if __name__ == "__main__":
    items = input("Enter items: ").split()
    print(find_duplicates(items))




