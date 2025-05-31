import threading

def evenfactor(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            total += i
    print("Sum of even factors: ",total)

def oddfactor(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            total += i
    print("Sum of odd factors: ", total)

def main():
    number = int(input("Eneter the number: "))

    T1 = threading.Thread(target=evenfactor, args=(number,))
    T2 = threading.Thread(target=oddfactor, args=(number,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
