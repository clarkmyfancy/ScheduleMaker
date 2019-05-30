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
	MARK_TASK_COMPLETED = 'c'
	# REMOVE_TASK_FROM_DB = 'r'


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
				fields = dao.getFieldsFromDB()
				records = dao.getRecordsFromDB()
				console.displayTodoListWithFieldsAndRecords(fields, records)

			elif selectedAction == programMode.MARK_TASK_COMPLETED.value:
				dao.markTaskCompletedWithId(taskID)
				pass

			# elif selectedAction == programMode.REMOVE_TASK_FROM_DB.value:
			# 	pass

			programShouldEnd = console.promptShouldProgramEndToUser()


if __name__ == '__main__':
	scheduleProgram = MainProgram()
	scheduleProgram.run()
