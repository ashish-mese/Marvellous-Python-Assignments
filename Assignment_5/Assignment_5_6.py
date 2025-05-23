def CtoF(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
   
    c = float(input("Enter temperature in Celsius: "))

    f = CtoF(c)

    print(f"temperature in Fahrenheit : {f}°F")


if __name__ == "__main__":
    main()