def main(age):

    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")


if __name__ == "__main__":
    age = int(input("Enter age: "))
    main(age)
