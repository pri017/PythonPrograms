def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

if __name__ == "__main__":
    s, e = map(int, input("Enter start and end: ").split())
    print(primes_in_range(s, e))





