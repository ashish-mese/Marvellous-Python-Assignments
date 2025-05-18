def addition (n):

    add = 0
    for i in (n):
        add = add + i

    return add   

def main(n):
    data = []
    for i in range (n):
        number = int(input("Enter number: ")) 
        data.append(number)

    return addition(data)

if __name__ == "__main__":

    n = int(input("Enter the size: "))
    ret = main(n)
    print(ret)
    
