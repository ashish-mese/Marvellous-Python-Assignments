import threading

def small(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    print("Thread Name: ", threading.current_thread(), "ID: ",threading.get_ident())
    print("Number of lowercase chars: ",count)

def capital(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    print("Thread Name: ", threading.current_thread(), "ID: ",threading.get_ident())
    print("Number of uppercase chars: ",count)

def digits(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    print("Thread Name: ", threading.current_thread(), "ID: ",threading.get_ident())
    print("Number of digits: ",count)

def main():
    paramater = input("Enter a string: ")

    T1 = threading.Thread(target=small, args=(paramater,))
    T2 = threading.Thread(target=capital, args=(paramater,))
    T3 = threading.Thread(target=digits, args=(paramater,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
