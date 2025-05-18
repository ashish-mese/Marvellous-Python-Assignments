from Arithmetic import *

def main(Val1, Val2):

    print (f"Addition of {Val1} and {Val2} is: ", Add(Val1, Val2))
    print (f"Subtraction of {Val1} and {Val2} is: ", Sub(Val1, Val2))
    print (f"Multiplication of {Val1} and {Val2} is: ", Mul(Val1, Val2))
    print (f"Division of {Val1} and {Val2} is: ", Div(Val1, Val2))

if __name__ == "__main__":
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))
    main(A,B)

