i = 1
def pattern(size):
    global i
    if i <= size:
        print(i*"* ", end = "")
        print()      
        i = i+1
        pattern(size)

def main():
    N = int(input("Enter the Number: "))
    pattern(N)
    
if __name__ == "__main__":
    main()