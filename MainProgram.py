# -- Modules
import datetime
import time
from enum import Enum

# --
from Console import *
from Task import *
from TaskDAO import *

class programMode(Enum):
	ADD_TASK_TO_DB = 'a'
	DISPLAY_TODO_LIST = 'd'

class MainProgram:

		# self.currentTime = datetime.datetime.now()

	def run(self):
		console = Console()
		dao = TaskDAO()
		programShouldEnd = False

		console.printStartScreen()

		while not programShouldEnd:
			selectedAction = console.promptStartSelectionToUser().lower()

			if selectedAction == programMode.ADD_TASK_TO_DB.value:
				(nm, typ, pri, endDate, descr) = console.getNewTaskDataFromUser()
				newTask = Task(nm, typ, pri, endDate, descr)
				dao.updateDBWithTask(newTask)

			elif selectedAction == programMode.DISPLAY_TODO_LIST.value:
				todoList = self.worksheet.get_all_records()
				console.displayList(todoList)

			programShouldEnd = console.promptShouldProgramEndToUser()


if __name__ == '__main__':
	scheduleProgram = MainProgram()
	scheduleProgram.run()
