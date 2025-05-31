import threading

def evenlist(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print("Sum of even elements: ", total)

def oddlist(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    print("Sum of odd elements: ", total)

def main():
    data = [11, 5, 22, 31, 10, 25, 16]

    T1 = threading.Thread(target=evenlist, args=(data,))
    T2 = threading.Thread(target=oddlist, args=(data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
