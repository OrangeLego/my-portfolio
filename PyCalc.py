from tkinter import *
from tkinter import messagebox

a = "null"
b = "null"

def number_clicked(number):
	global a, b

	if(a == "null" or b == "null"):
	        messagebox.showerror("Error", "Please enter two numbers first!")
        	return
	elif(a == "null"):
		a = float(number)
	elif(b == "null"):
		b = float(number)
	else:
		messagebox.showerror("General Error","You already have 2 vars, clear and try again!")

def operator_clicked(operator):
	if(operator == "+"):
		messagebox.showinfo("Result", float(a) + float(b))
	elif(operator == "-"):
		messagebox.showinfo("Result", float(a) - float(b))
	elif(operator == "*"):
		messagebox.showinfo("Result", float(a) * float(b))
	elif(operator == "/"):
		messagebox.showinfo("Result", float(a) / float(b))
	elif(operator == "%"):
		messagebox.showinfo("Result", float(a) % float(b))

def clear():
	global a, b
	a = "null"
	b = "null"

def main():
	root = Tk()
	root.title("Python Calculator")
	
	buttons = {}

	for i in range(1, 10):
		row, col = divmod(i-1, 3)
		buttons[i] = Button(root, text=str(i), command=lambda i=i: number_clicked(i))
		buttons[i].grid(row=row, column=col)

	buttons[0] = Button(root, text="0", command=lambda: number_clicked(0))
	buttons[0].grid(row=3, column=1)

	add_button = Button(root, text="+", command=lambda:operator_clicked("+"))
	minus_button = Button(root, text="-", command=lambda:operator_clicked("-"))
	multiply_button = Button(root, text="*", command=lambda:operator_clicked("*"))
	divide_button = Button(root, text="/", command=lambda:operator_clicked("/"))
	modulus_button = Button(root, text="%", command=lambda:operator_clicked("%"))
	clear_button = Button(root, text="Clear", command=clear)

	add_button.grid(row=0, column=3)
	minus_button.grid(row=1, column=3)
	multiply_button.grid(row=2, column=3)
	divide_button.grid(row=3, column=3)
	modulus_button.grid(row=4, column=3)
	clear_button.grid(row=5, column=3)

	root.mainloop()

if __name__ == "__main__":
	main()