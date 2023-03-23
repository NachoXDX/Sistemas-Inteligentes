primes = list(range(2,21))

def main():
    for n in range(2,21):
        for j in range(2,n):
            if n%j == 0:
                primes.remove(n)
                break
    print(primes)

if __name__ == "__main__":
    main()
            