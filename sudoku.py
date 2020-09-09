from tkinter import *
from random import *

root = Tk()
buttonWidth = 3
fields = []
field = [[0 for x in range(9)] for y in range(9)]

def close_window():
	root.destroy()

def readAllNumbers():
	for i in range(8):
		for k in range (8):
			field[i][k] = fields[(i * 10) + k].get()
			print(field[i][k])
	calculateSolution()

def calculateSolution():
	#print(checkRow(0, 0))
	print(checkBox(1, 0))
	#print(randint(0, 9))

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

def checkBox(column, row):
	verticalSection = 1
	horizontalSection = 1
	if (4 <= row <=6):
		verticalSection = 2
	if (7 <= row <= 9):
		verticalSection = 3

	if (4 <= row <=6):
		horizontalSection = 2
	if (7 <= row <= 9):
		horizontalSection = 3
	number = field[column][row]
	numberOfDuplicates = 0
	for i in range(9):
		if field[column][i] == number:
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
	button = Button(root, width = buttonWidth * 3, text = "QUIT", command = close_window)
	button.grid(row = 11, column = 0, columnspan = 2)

def setupComputeButton():
	button = Button(root, width = buttonWidth * 10, text = "COMPUTE", command = readAllNumbers)
	button.grid(row = 11, column = 2, columnspan = 7)


def main():
	setupFields()
	setupQuitButton()
	setupComputeButton()
	root.geometry("400x400")
	root.mainloop()

if __name__ == "__main__":
	main()