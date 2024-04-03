#the question not in middle
import easygui
easygui.buttonbox("What would you like to do?", choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], 
                  title="MENU MAKER OPTIONS")

msg = "What would you like to do?"
easygui.buttonbox(msg=msg.center(40), choices=["Add combo", "Find combo", "Delete combo", "Output all", "Exit"], 
                  title="MENU MAKER OPTIONS")