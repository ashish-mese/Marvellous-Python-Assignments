import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i, end = " ")
        time.sleep(1)
    print()

def main():
    
    T1 = threading.Thread(target=print_numbers)
    T2 = threading.Thread(target=print_numbers)
    T3 = threading.Thread(target=print_numbers)

    T1.start()
    T1.join()
    T2.start()
    T2.join()
    T3.start()
    T3.join()

   
    
    

    print("Exit from main.")

if __name__ == "__main__":
    main()
