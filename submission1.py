def main() -> None:
    num_of_nums: int = 10
    count: int = 1

    max_num = 0

    while count <= num_of_nums:
        curr_num: int = int(input(f"Enter number {count}: "))

        if curr_num > max_num:
            max_num = curr_num

        count += 1

    print(f"Max number: {max_num}")


if __name__ == "__main__":
    main()
