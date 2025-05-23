def main():
    num = 1
    total = 0

    while num <= 100:
        if num % 2 == 0:
            total += num
        num += 1
    
    print(f"Sum of even numbers between 1 to 100 is: {total}")


if __name__ == "__main__":
    main()