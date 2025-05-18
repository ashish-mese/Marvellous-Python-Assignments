from functools import reduce

def MyList(n):
    data = []
    for i in range (n):
        value = int(input("Enter numbers: "))
        data.append(value)
    print("***data**", data)
    return data

def main():
    num = int(input("Enter the size: "))
    list_data = MyList(num)

    print("**List Data**", list_data)

    fdata = list(filter(lambda x: 70<=x <=90, list_data))
    print("List after Filter: ", fdata)

    mdata = list(map(lambda x: x+10, fdata))
    print("List after Map: ", mdata)

    rdata = reduce(lambda x,y: x*y, mdata)
    print("Output of reduce: ", rdata)


if __name__ == "__main__":   
    main()

