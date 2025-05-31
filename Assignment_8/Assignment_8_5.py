import threading

def count():
    for i in range(1, 51):
        print(i, end=' ',)
    print("\nthread1 end")

def reverse():
    print("thread2 started")
    for i in range(50, 0, -1):
        print(i, end=' ')

def main():

    T1 = threading.Thread(target=count)

    T2 = threading.Thread(target=reverse)

    T1.start()
    T1.join()

    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
