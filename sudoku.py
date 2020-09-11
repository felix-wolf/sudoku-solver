from tkinter import *
from random import *

root = Tk()
buttonWidth = 3
fields = []
# field[COLUMN][ROW]
field = [[0 for x in range(9)] for y in range(9)]

def compute():
	readAllNumbers()
	calculateSolution()

def readAllNumbers():
	i = 0
	k = 0
	for item in fields:
		field[i][k] = item.get()
		i = i + 1
		if i is 9:
			i = 0
			k = k + 1

def calculateSolution():
	for i in range(9):
		for k in range (9):
			if field[i][k] == "":
				print("find Number")
			else:
				print("false")

def checkRow(column, row):
	number = field[column][row]
	numberOfDuplicates = 0
	for i in range(9):
		if field[column][i] == number:
			numberOfDuplicates +=1
	return numberOfDuplicates is 1

def checkColumn(column, row):
	number = field[column][row]
	numberOfDuplicates = 0
	for i in range(9):
		if field[i][row] == number:
			numberOfDuplicates +=1
	return numberOfDuplicates is 1

def setupFields():
	index = 0
	for i in range(9):
		for k in range (9):
			button = Entry(root, width = buttonWidth, text = str(index))
			button.grid(row = i, column = k)
			index = index + 1
			fields.append(button)

def setupQuitButton():
	button = Button(root, width = buttonWidth * 2, text = "QUIT", command = close_window)
	button.grid(row = 11, column = 0, columnspan = 2)

def setupComputeButton():
	button = Button(root, width = buttonWidth * 10, text = "COMPUTE", command = compute)
	button.grid(row = 11, column = 2, columnspan = 7)

def close_window():
	root.destroy()

def main():
	setupFields()
	setupQuitButton()
	setupComputeButton()
	root.geometry("400x400")
	root.mainloop()

if __name__ == "__main__":
	main()