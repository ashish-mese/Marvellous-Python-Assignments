import multiprocessing

def square(numbers):
    result = 0
    for i in numbers:
        result = i**2
        print (result, end = " ")

def main():
    numbers = [1, 2, 3, 4, 5]

    p = multiprocessing.Process(target=square, args=(numbers,))

    p.start()
    p.join()


if __name__ == "__main__":
    main()
