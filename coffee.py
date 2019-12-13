def main():
    print("Write how many cups of coffee you will need:", end=" ")
    cups = int(input())
    print(cups)

    print(f"For {cups} cups of coffee you will need:")

    print(f"{cups * 200} ml of water")
    print(f"{cups * 50} ml of milk")
    print(f"{cups * 15} g of coffee beans")

def machine_settings():
    print("Write how many ml of water the coffee machine has:", end=" ")
    water = int(input())

    print("Write how many ml of milk the coffee machine has:", end=" ")
    milk = int(input())

    print("Write how many grams of coffee beans the coffee machine has:", end=" ")
    beans = int(input())

    print("Write how many cups of coffee you will need:", end=" ")
    cups = int(input())

    theory_cups = evaluete_cups(water, milk, beans)

    if theory_cups > cups:
        print(f"Yes, I can make that amount of coffee (and even {theory_cups-cups} more than that)")
    elif cups == theory_cups:
        print(f"Yes, I can make that amount of coffee")
    else:
        print(f"No, I can make only {theory_cups} cups of coffee")

def evaluete_cups(water, milk, beans):
    wc = water // 200
    mc = milk // 50
    bc = beans // 15
    return min(wc, mc, bc)





if __name__ == "__main__":
    machine_settings()
