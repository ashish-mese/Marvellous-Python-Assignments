def Area(l, w):
    return l * w


def Perimeter(l, w):
    return 2 * (l+ w)

def main():
    
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))


    Rect_a = Area(length, width)
    Rect_p = Perimeter(length, width)


    print(f"\nArea: {Rect_a}")
    print(f"Perimeter: {Rect_p}")


if __name__ == "__main__":
    main()