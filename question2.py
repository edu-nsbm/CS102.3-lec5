# Print first 25 even numbers


def main() -> None:
    number: int = 2
    count: int = 0

    while count <= 24:
        print(number)
        count += 1
        number += 2


if __name__ == "__main__":
    main()
