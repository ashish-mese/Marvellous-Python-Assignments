def pattern(n):
    for i in range (n):
        print("* "*(n-i))

if __name__ == "__main__":

    n = int(input("Enter the size: "))
    pattern(n)

