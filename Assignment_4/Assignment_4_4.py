from functools import reduce

def MyList(n):
    data = []
    for i in range (n):
        value = int(input("Enter numbers: "))
        data.append(value)
    return data

def main():
    num = int(input("Enter the size: "))
    list_data = MyList(num)

    fdata = list(filter(lambda x: x % 2 == 0, list_data))
    print("List after Filter: ", fdata)

    mdata = list(map(lambda x: x**2, fdata))
    print("List after Map: ", mdata)

    rdata = reduce(lambda x,y: x+y, mdata)
    print("Output of reduce: ", rdata)


if __name__ == "__main__":   
    main()

