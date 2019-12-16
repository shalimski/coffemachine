class CoffeeMachine:
    def __init__(self, water=0, milk=0, coffee=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    @classmethod
    def coffee_params(cls, param):
        dict_param = {"1": (250, 0, 16, 1, 4),
                      "2": (350, 75, 20, 1, 7),
                      "3": (200, 100, 12, 1, 6)}
        return dict_param[param]

    def check_resourses(self, *res):
        water, milk, coffee, cups, money = res
        if self.water < water:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return False
        if self.coffee < coffee:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < cups:
            print("Sorry, not enough disposable cups!")
            return False
        return True

    def make_some_coffee(self, type_of_coffee):
        coffee_params = CoffeeMachine.coffee_params(type_of_coffee)
        if self.check_resourses(*coffee_params):
            self.water -= coffee_params[0]
            self.milk -= coffee_params[1]
            self.coffee -= coffee_params[2]
            self.cups -= coffee_params[3]
            self.money += coffee_params[4]
            print("I have enough resources, making you a coffee!")

    def action_buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:", end=" ")
        type_of_coffee = input()
        if type_of_coffee in "123":
            self.make_some_coffee(type_of_coffee)

    def action_fill(self):
        print("Write how many ml of water do you want to add:", end=" ")
        water = int(input())
        self.water += water

        print("Write how many ml of milk do you want to add:", end=" ")
        milk = int(input())
        self.milk += milk

        print("Write how many grams of coffee beans do you want to add: ", end=" ")
        coffee = int(input())
        self.coffee += coffee

        print("Write how many disposable cups of coffee do you want to add:", end=" ")
        cups = int(input())
        self.cups += cups

    def action_take(self):
        summ = self.money
        print(f"I gave you ${summ}")
        self.money = 0

    def print_status(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        print()

    def current_state(self):
        print("Write action (buy, fill, take, remaining, exit):", end=" ")
        self.act = input()


def main():
    m = CoffeeMachine(400, 540, 120, 9, 550)

    while True:
        m.current_state()

        if m.act == "buy":
            m.action_buy()
        elif m.act == "fill":
            m.action_fill()
        elif m.act == "take":
            m.action_take()
        elif m.act == "remaining":
            m.print_status()
        elif m.act == "exit":
            break


if __name__ == "__main__":
    main()
