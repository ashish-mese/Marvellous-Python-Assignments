import time
import threading
import multiprocessing

def Sum():
    total = 0
    for i in range(1, 10_000_001):
        total += i
    return total

def Normal():
    start = time.time()
    Sum()
    print("Normal function took:", time.time() - start)

def Threading():
    start = time.time()
    t = threading.Thread(target=Sum)
    t.start()
    t.join()
    print("Threading took:", time.time() - start)

def Multiprocessing():
    start = time.time()
    p = multiprocessing.Process(target=Sum)
    p.start()
    p.join()
    print("Multiprocessing took:", time.time() - start)

if __name__ == "__main__":
   
    Normal()
    Threading()
    Multiprocessing()