def main(N):
    data = []
    for i in range(N):
        Num = int(input("Enter the Number: "))
        data.append(Num)
    Even = list(filter(lambda N : N%2 == 0, data))
    return Even

if __name__ == "__main__":
    A = int(input("Enter the Size: "))
    Res = main(A)
    print("Even Number: ",Res)