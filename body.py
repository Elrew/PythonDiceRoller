import random
import tkinter
from tkinter import *
from tkinter import END, TOP, Button, Text, font
from tkinter.scrolledtext import ScrolledText
from turtle import width

main = tkinter.Tk()
main.geometry("700x500")
main.resizable(width=False,height=False)
main.title("Python Dice Roller")

# Used to keep each dropdown's value as it's own
clicked = tkinter.StringVar()
clicked2 = tkinter.StringVar()
clicked3 = tkinter.StringVar()
clicked4= tkinter.StringVar()
clicked5 = tkinter.StringVar()
clicked6 = tkinter.StringVar()
clicked7 = tkinter.StringVar()

# Creating the box for rolls to appear
rollbox = ScrolledText(width=75)
rollbox.pack(side=TOP, anchor="w",fill="y")


# Functions for calculating rolls
def calculate_rollD4():
    num = int(clicked.get())
    rollcount = int(clicked.get())
    while num > 0:
        rollbox.insert(END, f"D4 Roll {rollcount}: {random.randint(1,4)}\n"  )
        rollbox.see(END) 
        num = num -1
        rollcount = rollcount - 1

def calculate_rollD6():
    num = int(clicked2.get())
    rollcount = int(clicked2.get())
    while num > 0:
        rollbox.insert(END, f"D6 Roll {rollcount}: {random.randint(1,6)}\n"  )
        rollbox.see(END)  
        num = num -1
        rollcount = rollcount - 1

def calculate_rollD8():
    num = int(clicked3.get())
    rollcount = int(clicked3.get())
    while num > 0:
        rollbox.insert(END, f"D8 Roll {rollcount}: {random.randint(1,8)}\n"  )
        rollbox.see(END)  
        num = num -1
        rollcount = rollcount - 1

def calculate_rollD10():
    num = int(clicked4.get())
    rollcount = int(clicked4.get())
    while num > 0:
        rollbox.insert(END, f"D10 Roll {rollcount}: {random.randint(1,10)}\n"  )
        rollbox.see(END)  
        num = num -1
        rollcount = rollcount - 1

def calculate_rollD00():
    num = int(clicked5.get())
    rollcount = int(clicked5.get())
    while num > 0:
        rollbox.insert(END, f"D00 Roll {rollcount}: {random.randint(1,10)}0\n"  )
        rollbox.see(END)  
        num = num -1
        rollcount = rollcount - 1

def calculate_rollD12():
    num = int(clicked6.get())
    rollcount = int(clicked6.get())
    while num > 0:
        rollbox.insert(END, f"D12 Roll {rollcount}: {random.randint(1,12)}\n"  )
        rollbox.see(END)  
        num = num -1
        rollcount = rollcount - 1

def calculate_rollD20():
    num = int(clicked7.get())
    rollcount = int(clicked7.get())
    while num > 0:
        rollbox.insert(END, f"D20 Roll {rollcount}: {random.randint(1,20)}\n"  )
        rollbox.see(END)  
        num = num -1
        rollcount = rollcount - 1

# Options for the drop down menus
options = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]


# Creates Dropdowns for the quantity of dice
dropdownD4 = tkinter.OptionMenu(main, clicked, *options)
dropdownD6 = tkinter.OptionMenu(main, clicked2, *options)
dropdownD8 = tkinter.OptionMenu(main, clicked3, *options)
dropdownD10 = tkinter.OptionMenu(main, clicked4, *options)
dropdownD00 = tkinter.OptionMenu(main, clicked5, *options)
dropdownD12 = tkinter.OptionMenu(main, clicked6, *options)
dropdownD20 = tkinter.OptionMenu(main, clicked7, *options)
dropdownD4.config(width="9")
dropdownD6.config(width="9")
dropdownD8.config(width="9")
dropdownD10.config(width="9")
dropdownD00.config(width="9")
dropdownD12.config(width="9")
dropdownD20.config(width="9")
# Sorts the dropdowns
dropdownD4.pack(side = tkinter.LEFT, anchor="s", )
dropdownD6.pack(side = tkinter.LEFT, anchor="s", )
dropdownD8.pack(side = tkinter.LEFT, anchor="s", )
dropdownD10.pack(side = tkinter.LEFT, anchor="s", )
dropdownD00.pack(side = tkinter.LEFT, anchor="s", )
dropdownD12.pack(side = tkinter.LEFT, anchor="s", )
dropdownD20.pack(side = tkinter.LEFT, anchor="s", )

# Buttons to click to roll the die for them 
helv22 = font.Font(family='Helvetica', size=22, weight=font.BOLD)
buttonD4 =tkinter.Button(main, text="D4", command=calculate_rollD4, font=helv22)
buttonD6 =tkinter.Button(main, text="D6", command=calculate_rollD6, font=helv22 )
buttonD8 =tkinter.Button(main, text="D8", command=calculate_rollD8, font=helv22 )
buttonD10 =tkinter.Button(main, text="D10", command=calculate_rollD10, font=helv22 )
buttonD00 =tkinter.Button(main, text="D00", command=calculate_rollD00, font=helv22 )
buttonD12 =tkinter.Button(main, text="D12", command=calculate_rollD12, font=helv22 )
buttonD20 =tkinter.Button(main, text="D20", command=calculate_rollD20, font=helv22 )


# Button placement
buttonD4.pack(side = tkinter.LEFT, anchor="s", )
buttonD6.pack(side = tkinter.LEFT, anchor="s", )
buttonD8.pack(side = tkinter.LEFT, anchor="s", )
buttonD10.pack(side = tkinter.LEFT, anchor="s", )
buttonD00.pack(side = tkinter.LEFT, anchor="s", )
buttonD12.pack(side = tkinter.LEFT, anchor="s", )
buttonD20.pack(side = tkinter.LEFT, anchor="s", )
buttonD4.place(bordermode=tkinter.OUTSIDE,x=15, y=408)
buttonD6.place(bordermode=tkinter.OUTSIDE,x=115, y=408)
buttonD8.place(bordermode=tkinter.OUTSIDE,x=220, y=408)
buttonD10.place(bordermode=tkinter.OUTSIDE,x=310, y=408)
buttonD00.place(bordermode=tkinter.OUTSIDE,x=409, y=408)
buttonD12.place(bordermode=tkinter.OUTSIDE,x=507, y=408)
buttonD20.place(bordermode=tkinter.OUTSIDE,x=605, y=408)


# Darkmode button

# buttons replaced with images 

# roll with advant and disadvant 
# rollbox font settings

# clear all rolls button

def clear_rollbox():
    rollbox.delete('1.0',END)


clear_button = tkinter.Button(
    main,
    text='Clear',
    width="6",
    command=clear_rollbox
)

# exit button
exit_button = tkinter.Button(
    main,
    text='Exit',
    width="6",
    command=lambda: main.quit()
)

exit_button.place(in_=rollbox, x= "647",y="350")
clear_button.place(in_=rollbox,x= "647",y="310")





# Adding light and dark mode images
light = tkinter.PhotoImage(file="light.png")
dark = tkinter.PhotoImage(file="dark.png")

switch_value = True

# Defining a function to toggle
# between light and dark theme
def toggle():

	global switch_value
	if switch_value == True:
		switch.config(image=dark, bg="#26242f",
					activebackground="#26242f")
		rollbox.config(bg="#26242f", fg="white")
		# Changes the window to dark theme
		main.config(bg="#26242f")
		switch_value = False

	else:
		switch.config(image=light, bg="white",
					activebackground="white")
		rollbox.config(bg="white", fg="black")
		# Changes the window to light theme
		main.config(bg="white")
		switch_value = True


# Creating a button to toggle
# between light and dark themes
switch = Button(main, image=light,
				bd=0, bg="white",
				activebackground="white",
				command=toggle)
switch.place(in_=rollbox,x= "647",y="270")


main.mainloop()
