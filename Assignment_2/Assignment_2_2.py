def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end = " ")

        print()
if __name__ == "__main__":
    n = int(input("Enter the pattern size: "))
    pattern(n)