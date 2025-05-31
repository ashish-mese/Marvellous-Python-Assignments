import multiprocessing

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    numbers = [3, 4, 5, 6, 7]

    pool =multiprocessing.Pool()
    results = pool.map(factorial, numbers)

    print("Input Numbers:", numbers)
    print("Factorials:", results)


if __name__ == "__main__":
    main()
