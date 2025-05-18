def frequency (n):
    check = int(input("Enter number to check frequency: "))
    count = 0
    for i in (n):
        if i == check:
            count=count+1
        
    return count   

def main(n):
    data = []
    for i in range (n):
        number = int(input("Enter number: "))
        data.append(number)

    return frequency(data)

if __name__ == "__main__":

    n = int(input("Enter the size: "))
    ret = main(n)
    print(ret)
    
