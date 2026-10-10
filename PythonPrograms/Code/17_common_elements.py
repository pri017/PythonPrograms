def common_elements(lst1, lst2):
    return sorted(list(set(lst1) & set(lst2)))

if __name__ == "__main__":
    l1 = input("Enter list 1: ").split()
    l2 = input("Enter list 2: ").split()
    print(common_elements(l1, l2))