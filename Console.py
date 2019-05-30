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
		print("Enter \"C\" to enter section to mark a task as completed.")
		# print("Enter \"R\" to remove a task from the todo list.")
		print("--> ", end="")
		userSelection = input()
		print()
		return userSelection

	def getNewTaskDataFromUser(self):
		print("Enter the name of the task.")
		print("--> ", end="")
		name = input()
		print("Enter the type of the task.")
		print("--> ", end="")
		type = input()
		print("Enter the priority of the task.")
		print("--> ", end="")
		priority = input()
		print("Enter the completion date of the task with the time.")
		print("--> ", end="")
		finishByDateTime = input()
		print("Enter the task's description.")
		print("--> ", end="")
		descr = input()
		print()
		return (name, type, priority, finishByDateTime, descr)

	def displayTodoListWithFieldsAndRecords(self, fields, records):
		print("TASK" + "\t\t| " + fields[5].upper())
		dashes = ""
		for x in range(0, 100):
			dashes += "-"
		print(dashes)
		for x in records:
			if (len(x) < len(fields)):
				print(x[0] + "\t|")
			else:
				print(x[0] + "\t| " + x[5])
			print(dashes)
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
