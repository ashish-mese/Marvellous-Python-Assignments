def main():
    num = int(input("Enter a number: "))

    print(f"\nMultiplication table of {num}:\n")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

if __name__ == "__main__":
    main()