from tkinter import *
import os

#have a list of characters so the user can navigate through the list
#whenever it reaches a character index it will randomly select an image of that character to use so there can be some funny stuff

#Ignore this
character_list = ["Noob", ""]

script_dir = os.path.dirname(os.path.abspath(__file__)) 
print("SCRIPT DIRECTORY: ", script_dir)

def write_to_file(string):
    path = os.path.join(script_dir, "Character.txt")
    with open(path, "w") as file:
        file.write(string)

def get_current_character():
    match button.get():
        case 0:
            print("You are Noob!")
            write_to_file("Noob")
        case 1:
            print("You are 007n7!")
            write_to_file("007n7")
        case 2:
            print("You are Veeronica!")
            write_to_file("Veeronica")
        case 3:
            print("You are Guest!")
            write_to_file("Guest")
        case 4:
            print("You are Chance!")
            write_to_file("Chance")
        case 5:
            print("You are Two Time!")
            write_to_file("Two Time")
        case 6:
            print("You are Dusekkar!")
            write_to_file("Dusekkar")
        case 7:
            print("You are Builderman!")
            write_to_file("Builderman")
        case 8:
            print("You are Shedletsky!")
            write_to_file("Shedletsky")
        case 9:
            print("You are Elliot!")
            write_to_file("Elliot")
        case 10:
            print("You are Jane Doe!")
            write_to_file("Jane Doe")
        case 11:
            print("You are Taph!")
            write_to_file("Taph")



character_names = ["Noob", "007n7", "Veeronica", 
"Guest 1337", "Chance", "Two Time", 
"Dusekkar", "Builderman", "Shedletsky", 
"Elliot", "Jane Doe", "Taph"]

def create_label(character, row_num):
    label = Label(window, text=character, anchor=W).grid(row=row_num, column=0)
    Radiobutton(window, variable=button, value=row_num, command=get_current_character, anchor=W).grid(row=row_num, column=1)


window = Tk()
window.geometry("420x420")
window.title("Character Selector")

button = IntVar()

row = 0

for character in character_names:
    create_label(character, row)
    row += 1


window.mainloop()
