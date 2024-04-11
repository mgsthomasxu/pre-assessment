def get_valid_price(prompt):
    while True:
        price = easygui.enterbox(prompt)
        if price is None:
            return None
        try:
            price = float(price)
            if price >= 0:
                return price
            else:
                easygui.msgbox("Price must be a non-negative number.")
        except ValueError:
            easygui.msgbox("Invalid price. Please enter a valid number.")

def calculate_total_price(items):
    return sum(items.values())

# main menu
import easygui

combos = {"Value Meal": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
          "Cheezy Meal": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
          "Super Meal": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}

easygui.buttonbox("What would you like to do?", 
                  choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], 
                  title="MENU MAKER OPTIONS")

while True:
    choice = easygui.buttonbox("What would you like to do?", 
                                choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], 
                                title="MENU MAKER OPTIONS")

    if choice == "Add combo":
        combo_name = easygui.enterbox("Enter the name of the combo:")
        if combo_name:
            items = {}
            while True:
                item_name = easygui.enterbox(f"Enter the item name for {combo_name} (or leave blank to finish):")
                if not item_name:
                    break
                item_price = get_valid_price(f"Enter the price for {item_name}:")
                if item_price is None:
                    break
                items[item_name] = float(item_price)
            combos[combo_name] = items
            easygui.msgbox(f"{combo_name} added successfully!")

    elif choice == "Find combo":
        combo_name = easygui.enterbox("Enter the name of the combo to find:")
        if combo_name in combos:
            items = combos[combo_name]
            item_details = "\n".join([f"{item}: ${price}" for item, price in items.items()])
            total_price = calculate_total_price(items)
            easygui.msgbox(f"{combo_name} Details:\n{item_details}")
        else:
            easygui.msgbox(f"Combo '{combo_name}' not found!")

    elif choice == "Delete combo":
        combo_name = easygui.enterbox("Enter the name of the combo to delete:")
        if combo_name in combos:
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