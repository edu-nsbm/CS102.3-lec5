def main() -> None:
    num_of_units: int = int(input("Enter no of units: "))

    compulsary_tax: float = 1000
    unit_cost: float = 0
    total: float = 0

    if num_of_units <= 50:
        unit_cost = num_of_units * 50
    elif num_of_units <= 100:
        unit_cost = 50 * 50 + (num_of_units - 50) * 100
    else:
        unit_cost = 50 * 50 + 50 * 100 + (num_of_units - 100) * 150

    total = unit_cost + compulsary_tax

    print(f"Total cosrt: {total}LKR")


if __name__ == "__main__":
    main()
