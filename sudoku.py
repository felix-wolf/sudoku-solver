from tkinter import *
from random import *

root = Tk()
buttonWidth = 2
fields = []
# field[COLUMN][ROW]
field = [[0 for x in range(9)] for y in range(9)]

def compute():
	processFields("clear")
	processFields("read")
	calculateSolution()
	print("done")
	processFields("write")

def processFields(mode):
	i = 0
	k = 0
	for item in fields:
		if (mode is "clear"):
			item.delete(0, END)
		if (mode is "write"):
			field[i][k] = item.insert(0, str(field[i][k]))
		if (mode is "read"):
			field[i][k] = item.get()
		i = i + 1
		if i is 9:
			i = 0
			k = k + 1

def calculateSolution():
	calculate(0, 0)

def calculate(row, column):
	if (row == 8) and (column == 8):
		return
	if (field[column][row] == ""):
		field[column][row] = findSolution(row, column)
	column = column + 1
	if column is 9:
		column = 0
		row = row + 1

	print(checkRow(column, row))
	calculate(row, column)

def findSolution(row, column):
	numbers = [1,2,3,4,5,6,7,8,9]
	for number in numbers:
		if isNotValid(row, column, number):
			numbers.remove(number)
	return choice(numbers)

def isNotValid(row, column, number):
	isInRow = False
	isInColumn = False
	for i in range(9):
		if field[i][row] == number:
			isInRow = True
		if field[column][i] == number:
			isInColumn = True
	return isInColumn or isInRow


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