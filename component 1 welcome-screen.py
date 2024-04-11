###component 1 welcome-screen


#bring in easygui
import easygui

#dictionary for the combos given
combos = {"Value Meal": {"Beef burger": 5.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
          "Cheezy Meal": {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy drink": 1.00}, 
          "Super Meal": {"Cheeseburger": 6.69, "Large fries": 2.00, "Smoothie": 2.00}}

#Main Menu
choices = easygui.buttonbox("What would you like to do?", choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], 
                  title="MENU MAKER OPTIONS")



 #choice buttons
if choices == "Add combo":
    combo_name = easygui.enterbox("Enter the name of the combo:")
    item_name = easygui.enterbox(f"Enter the item name for {combo_name} (or leave blank to finish):")
    item_price = easygui.enterbox(f"Enter the price for {item_name}:")