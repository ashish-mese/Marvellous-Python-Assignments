def Large():
   
    numbers = list(map(int, input("Enter 5 numbers: ").split()))

    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num

    return largest

if __name__ == "__main__":
    Res = Large()
    print(f"Maximum number is: {Res}")