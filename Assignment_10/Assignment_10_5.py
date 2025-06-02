from functools import reduce

def MyList(n):
    data = []
    for i in range (n):
        value = int(input("Enter numbers: "))
        data.append(value)
    return data

def ChkPrime(n):
    if n ==2:
        return True
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def maximum(x,y):
    if x>y:
        return x
    
    else:
        return y
        
        

def main():
    num = int(input("Enter the size: "))
    list_data = MyList(num)

    fdata = list(filter(ChkPrime, list_data))
    print("List after Filter: ", fdata)

    mdata = list(map(lambda x: x*2, fdata))
    print("List after Map: ", mdata)

    rdata = reduce(maximum, mdata)
    print("Output of reduce: ", rdata)


if __name__ == "__main__":   
    main()