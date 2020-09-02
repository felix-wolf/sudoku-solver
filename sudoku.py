from tkinter import *

root = Tk()
buttonWidth = 3
fields = []
rows = [[]]

def close_window():
	root.destroy()

def compute():
	for entry in fields:
		print(entry.get())

def setupFields():
	index = 0
	for i in range(9):
		for k in range (9):
			button = Entry(root, width = buttonWidth, text = str(index))
			button.grid(row = i, column = k)
			index = index + 1
			fields.append(button)

def setupQuitButton():
	button = Button(root, width = buttonWidth * 3, text = "QUIT", command = close_window)
	button.grid(row = 11, column = 0, columnspan = 2)

def setupComputeButton():
	button = Button(root, width = buttonWidth * 10, text = "COMPUTE", command = compute)
	button.grid(row = 11, column = 2, columnspan = 7)


def main():
	setupFields()
	setupQuitButton()
	setupComputeButton()
	root.geometry("400x400")
	root.mainloop()

if __name__ == "__main__":
	main()