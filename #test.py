import easygui

combos = {"Value Meal": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
          "Cheezy Meal": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
          "Super Meal": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}

def get_valid_price(prompt):
    while True:
        price_str = easygui.enterbox(prompt) if (price_str := easygui.enterbox(prompt)) is not None and price_str.isnumeric() else None
        return price_str

def calculate_total_price(items):
    return sum(items.values())

while True:
    choice = easygui.buttonbox("What would you like to do?", choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], title="MENU MAKER OPTIONS")

    if choice == "Add combo":
        if (combo_name := easygui.enterbox("Enter the name of the combo:")):
            items = {}
            while True:
                if not (item_name := easygui.enterbox(f"Enter the item name for {combo_name} (or leave blank to finish):")):
                    break
                if (item_price := get_valid_price(f"Enter the price for {item_name}:")) is None:
                    break
                items[item_name] = float(item_price)
            combos[combo_name] = items
            easygui.msgbox(f"{combo_name} added successfully!")

    elif choice == "Find combo":
        if (combo_name := easygui.enterbox("Enter the name of the combo to find:")) in combos:
            items = combos[combo_name]
            item_details = "\n".join([f"{item}: ${price}" for item, price in items.items()])
            total_price = calculate_total_price(items)
            easygui.msgbox(f"{combo_name} Details:\n{item_details}")
        else:
            easygui.msgbox(f"Combo '{combo_name}' not found!")

    elif choice == "Delete combo":
        if (combo_name := easygui.enterbox("Enter the name of the combo to delete:")) in combos:
            del combos[combo_name]
            easygui.msgbox(f"{combo_name} deleted successfully!")
        else:
            easygui.msgbox(f"Combo '{combo_name}' not found!")

    elif choice == "Output all":
        message = "Combo Meals:\n\n"
        for combo_name, items in combos.items():
            message += f"{combo_name}:\n"
            for item, price in items.items():
                message += f"    - {item}: ${price}\n"
        easygui.msgbox(message, title="Combo Meals")

    elif choice == "Exit":
        break