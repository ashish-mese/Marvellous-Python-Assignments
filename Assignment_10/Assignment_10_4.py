from functools import reduce

def main ():

    data = list(map(int, input(" Enter numbers with space: ").split()))

    fdata = list(filter(lambda x: x%2 == 0, data ))
    print ("Filtered even numbers: ", fdata)

    mdata = list(map(lambda x: x**2, fdata))
    print("Map data after power of 2: ", mdata)

    rdata = reduce(lambda x,y: x+y, mdata)
    print("Addition of mapped data using reduce", rdata)
if __name__ == "__main__":

    main()