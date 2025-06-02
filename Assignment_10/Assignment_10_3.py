from functools import reduce

def my_list(n):
    data = []
    for i in range (n+1):
        value = int(input("Enter numbers: "))
        data.append(value)
    return data

def main():
    num = int(input("Enter size of list: "))
    list_data = my_list(num)

    fdata = list(filter(lambda x: 70<= x <= 90, list_data))
    print("List after filter: ", fdata)

    mdata = list(map(lambda x: x+10 , fdata))
    print("List after map: ", mdata)

    rdata = reduce(lambda x,y:(x*y), mdata)
    print("List after reduce: ", rdata)

if __name__ == "__main__":

    main()