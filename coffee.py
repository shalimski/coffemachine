def main():
    print("Write how many cups of coffee you will need:", end=" ")
    cups = int(input())
    print(cups)

    print(f"For {cups} cups of coffee you will need:")

    print(f"{cups * 200} ml of water")
    print(f"{cups * 50} ml of milk")
    print(f"{cups * 15} g of coffee beans")

if __name__ == "__main__":
    main()
