###component 1 welcome-screen###

#Bring in easygui
import easygui

#Dictionary for the combos given
combos = {
    "Value Meal": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
    "Cheezy Meal": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
    "Super Meal": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}
}

#Main Menu
choices = easygui.buttonbox("What would you like to do?", choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], title="MENU MAKER OPTIONS")

#Choice buttons
#What you need to put in when you have pressed add combo button
while True:
    if choices == "Add combo":
        combo_name = easygui.enterbox("Enter the name of the combo:")
        item_name = easygui.enterbox(f"Enter the item name for {combo_name} (or leave blank to finish):")
        item_price = easygui.integerbox(f"Enter the price for {item_name}:")
    #What you need to put in when you have pressed find combo button
    elif choices == "Find combo":
        combo_name = easygui.enterbox("Enter the name of the combo to find:")
    #What you need to put in when you have pressed delete combo
    elif choices == "Delete combo":
        combo_name = easygui.enterbox("Enter the name of the combo to delete:")
    #When pressed output all need to show all combos including the added combos (if delete combos no need to show)
    elif choices == "Output all":
        print(f"{combo_name, item_name, item_price}")
    #Exit program
    elif choices == "Exit":
        break