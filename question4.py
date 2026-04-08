# Write a program to find the factorial of a number


def main() -> None:
    number: int = int(input("Enter number: "))
    factorial: int = 1

    while number > 1:
        factorial *= number
        number -= 1

    print(f"Factorial of {number} is: {factorial}")


if __name__ == "__main__":
    main()
