class Console:

	def __init__(self):
		pass

	def printStartScreen(self):
		print()
		print("Welcome to Schedule Maker©")
		print()

	def promptStartSelectionToUser(self):
		print("Enter \"A\" to add a task to the todo list.")
		print("Enter \"D\" to display the current todo list.")
		print("Enter \"P\" to view prioritized todo list.")
		userSelection = input()
		print()
		return userSelection

		# user input is always scary, this should have error correction
	def getNewTaskDataFromUser(self):
		name = input("Enter the name of the task: ")
		type = input("Enter the type of the task: ")
		priority = input("Enter the priority of the task: ")
		finishByDateTime = input("Enter the completion date with format \"yyyy-dd-mm hh:mm:ss\": ")
			# if no time given could assume the time is like 7pm or something
		descr = input("Enter the task's description: ")
		print()
		return (name, type, priority, finishByDateTime, descr)

	def displayList(self, todoList):
		for x in todoList:
			print(x)
		print()

	def promptShouldProgramEndToUser(self):
		programShouldEnd = True
		programShouldNotEnd = False
		userInput = input("Enter any key to continue, or x to quit: ").lower()
		print()
		if userInput == 'x':
			return programShouldEnd
		else:
			return programShouldNotEnd
