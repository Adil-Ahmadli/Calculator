# Python program to create a simple GUI calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
expression = "" 


# Function to update expression in the text entry box 
def press(num): 
	global expression 
	expression = expression + str(num) 
	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used  for handling the errors like zero division error etc. 
	try: 

		global expression  
		total = str(eval(expression)) 
		equation.set(total)  
		expression = "" 

	# if error is generate then handle by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	#gui.configure() 

	# set the title of GUI window 
	gui.title("Simple Calculator") 


	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for showing the expression . 
	expression_field = Entry( gui, font=('arial',20, 'bold') , textvariable=equation, bd=20, insertwidth=4, bg="powder blue", justify="right" ) 

	# grid method is used for placing the widgets at respective positions in table like structure . 
	expression_field.grid(columnspan=4)

	# create a Buttons and place at a particular  location inside the root window . 
	# when user press the button, the command or  function affiliated to that button is executed . 
	button1 = Button(gui, text="1", padx=22, pady=16, bd=8,  fg='black', font=("arial", 20, "bold"), bg="powder blue", command=lambda: press(1)) 
	button1.grid(row=1, column=0)

	button2 = Button(gui, text="2", padx=22,pady=16, bd=8,  fg='black', bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(2)) 
	button2.grid(row=1, column=1)

	button3 = Button(gui, text="3", padx=22,pady=16, bd=8,  fg='black', bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(3)) 
	button3.grid(row=1, column=2)

	button4 = Button(gui, text="4", padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(4)) 
	button4.grid(row=2, column=0) 

	button5 = Button(gui, text="5", padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(5)) 
	button5.grid(row=2, column=1) 

	button6 = Button(gui, text="6"  ,padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"), command=lambda: press(6) ) 
	button6.grid(row=2, column=2) 

	button7 = Button(gui, text="7", padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"), command=lambda: press(7)) 
	button7.grid(row=3, column=0) 

	button8 = Button(gui, text="8" ,padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(8)) 
	button8.grid(row=3, column=1) 

	button9 = Button(gui, text="9", padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(9)) 
	button9.grid(row=3, column=2) 

	button0 = Button(gui, text="0", padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press(0)) 
	button0.grid(row=4, column=0) 

	plus = Button(gui, text='+', padx=22, pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),	command=lambda: press("+")) 
	plus.grid(row=1, column=3) 

	minus = Button(gui, text='-', padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press("-")) 
	minus.grid(row=2, column=3) 

	multiply = Button(gui, text='*', padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press("*")) 
	multiply.grid(row=3, column=3) 

	divide = Button(gui, text='/', padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=lambda: press("/")) 
	divide.grid(row=4, column=3) 

	equal = Button(gui, text='=', padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),command=equalpress) 
	equal.grid(row=4, column=2) 

	clear = Button(gui, text='C', padx=22,pady=16, bd=8, fg='black',bg="powder blue", font=("arial", 20, "bold"),	command=clear) 
	clear.grid(row=4, column=1) 

	#Decimal= Button(gui, text='.', padx=16, bd=8, fg='black', font=("arial", 20, "bold"),command=lambda: press('.')) 
	#Decimal.grid(row=6, column=0) 
	# start the GUI 
	gui.mainloop()
