from MarvellousNum import ChkPrime

def ListPrime(Val):
    prime =[]
    for i in (Val):
        if ChkPrime(i) == True:
            prime.append(i)
    return sum(prime)

def main(n):
    data = []
    for i in range (n):
        numbers= int(input("ENter number: "))
        data.append(numbers)

    return ListPrime(data)


if __name__ == "__main__":

    n = int(input("Enter the size: "))
    ret = main(n)
    print(ret)