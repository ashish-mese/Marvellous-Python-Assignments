def minimum (n):
    small = n[0]
    for i in (n[1:]):
        
        if i < small:
            small = i
        
    return small   

def main(n):
    data = []
    for i in range (n):
        number = int(input("Enter number: "))
        data.append(number)

    return minimum(data)

if __name__ == "__main__":

    n = int(input("Enter the size: "))
    ret = main(n)
    print(ret)
    
