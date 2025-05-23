def main(N):
    data = []
    for i in range(N):
        Num = int(input("Enter the Number: "))
        data.append(Num)
    double = list(map(lambda N : N*2, data))
    return double

if __name__ == "__main__":
    A = int(input("Enter the Size: "))
    Res = main(A)
    print("Double List: ",Res)