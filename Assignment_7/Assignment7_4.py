from functools import reduce

def main(N):
    data = []
    for i in range(N):
        Num = int(input("Enter the Number: "))
        data.append(Num)
    double = reduce(lambda X,Y : X*Y, data)
    return double

if __name__ == "__main__":
    A = int(input("Enter the Size: "))
    Res = main(A)
    print("Product: ",Res)