def show_inventory(inventory):
    print()
    print("Current Inventory:")
    for fruit, stock in inventory.items():
        print(f"{fruit}: {stock}")
    print()


def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory:
        print(f"{fruit} already exists!")
        print()
    else:
        stock = int(input(f"Enter stock for {fruit}: "))
        inventory[fruit] = stock
        print(f"{fruit} added with stock {stock}.")
        print()


def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    if fruit in inventory:
        amount = int(input(f"Enter amount to add to {fruit}'s stock: "))
        inventory[fruit] += amount
        print(f"{fruit} stock increased by {amount}.")
        print()
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.")
        print()


def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")


def run_program():
    inventory = {
        "apples": 10,
        "bananas": 20,
        "oranges": 15
    }

    print("Welcome to the Fruit Shop!")
    print()

    while True:
        menu()
        option = input("Enter option number: ")

        if option == "1":
            show_inventory(inventory)
        elif option == "2":
            add_fruit(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            print("Goodbye!")
            break
    # FREEZE CODE END
