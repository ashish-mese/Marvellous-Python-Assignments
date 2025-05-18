def maximum (n):
    large = n[0]
    for i in (n[1:]):
        if i >= large:
            large=i
        
    return large   

def main(n):
    data = []
    for i in range (n):
        number = int(input("Enter number: "))
        data.append(number)

    return maximum(data)

if __name__ == "__main__":

    n = int(input("Enter the size: "))
    ret = main(n)
    print(ret)
    
