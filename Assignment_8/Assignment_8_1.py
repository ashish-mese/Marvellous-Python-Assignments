import threading

def even(size):
    even_list =[]
    count = 0
    num = 1
    while count < size:
        if num % 2 == 0:
            even_list.append(num)
            count += 1
        num += 1
    print(even_list)

def odd(size):
    odd_list = []
    count = 0
    num = 1
    while count < size:
        if num % 2 != 0:
            odd_list.append(num)
            count += 1
        num += 1
    print(odd_list)

def main():

    T1 = threading.Thread(target=even, args=(10,))
    T2 = threading.Thread(target=odd, args=(10,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()
