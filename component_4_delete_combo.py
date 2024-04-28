###component 4 add combos###

import easygui
#Dictionary for the combos given
combos = {
    "Value Meal": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
    "Cheezy Meal": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
    "Super Meal": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}
}


#Main Menu
choices = easygui.buttonbox("What would you like to do?", choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], title="MENU MAKER OPTIONS")


#loop to keep the program running until the user chooses to exit
while True:
    if choices == "Add combo":
        combo_name = easygui.enterbox("Enter combo name:")
        #If a name is provided, continue
        if combo_name:  
            new_combo = {}
            while True:
                item_name = easygui.enterbox(f"Enter {combo_name} item name (leave blank to finish):")
                #Exit if no item name is provided
                if not item_name:
                    break  
                item_price = easygui.enterbox(f"Price for {item_name}:")
                if item_price:
                    new_combo[item_name] = float(item_price)
            #Add the new combo to the dictionary
            combos[combo_name] = new_combo  
            easygui.msgbox(f"{combo_name} added successfully!")
    elif choices == "Find combo":
        #Ask for combo name to find
        combo_name = easygui.enterbox("Enter the name of the combo to find:")
        if combo_name in combos:
            #If combo exists, get its items
            items = combos[combo_name]
            #Format item details for display
            item_details = "\n".join([f"{item}: ${price}" for item, price in items.items()])
            easygui.msgbox(f"{combo_name} Details:\n{item_details}")
        else:
            # If combo doesn't exist, show error message
            easygui.msgbox(f"Combo '{combo_name}' not found!")