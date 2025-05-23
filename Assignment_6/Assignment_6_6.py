def Star(N):
    for i in range(1, N + 1):         
        for j in range(1, i + 1):       
            print("*", end=" ")
        print()  

if __name__ == "__main__":

    Pattern = int(input("Enter the number of rows: "))
    Star(Pattern)