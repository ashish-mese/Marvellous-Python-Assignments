def add(n):
    addition = 0
    for i in (n):
        addition = addition + int(i)
    return addition

if __name__ == "__main__":

    n = input("Enter the number: ")
    ret=add(n)
    print(ret)
    

