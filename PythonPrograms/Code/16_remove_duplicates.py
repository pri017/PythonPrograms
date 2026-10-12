def remove_duplicates(lst):
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

if __name__ == "__main__":
    items = input("Enter items: ").split()
    print(remove_duplicates(items))



