# Print the following sequence
#     -36, -30, -24, -18, ... , 30, 36, 42
#     81, 72, 63, ... , -18, -27


def main3() -> None:
    count: int = 1

    while count <= 10:
        print(count * count)
        count += 1


def main2() -> None:
    count: int = 81

    while count >= -27:
        print(count)
        count -= 9


def main1() -> None:
    count: int = -36

    while count <= 42:
        print(count)
        count += 6


if __name__ == "__main__":
    main1()

    print()
    print()

    main2()

    print()
    print()

    main3()
