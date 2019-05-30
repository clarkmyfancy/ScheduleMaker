# -- APIs
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

class TaskDAO():

	def __init__(self):
		'''
			this should be inside of a try catch finally block becuase
				what happens when the internet is not working?
			for right now will get a working version with gsheets
				adn then worry about storing this offline
		'''
		self.scope = ['https://www.googleapis.com/auth/drive']
		self.serviceAccountCreds = SAC.from_json_keyfile_name('Scheduler-30eefa3a4c69.json', self.scope)
		self.gc = gspread.authorize(self.serviceAccountCreds)
		self.worksheet = self.gc.open('taskDB')
		self.incompleteTasksWorksheet = self.worksheet.worksheet('Incomplete Tasks')
		# self.incompleteTasksWorksheet = self.gc.open('taskDB').sheet1
		# self.completeTasksWorksheet = self.gc.open('taskDB').sheet2
		self.numIncompleteTasks = len(self.incompleteTasksWorksheet.col_values(1)) - 1
		# self.numCompleteTasks = len(self.completeTasksWorksheet.col_values(1)) - 1

	def updateDBWithTask(self, newTask):
		firstEmptyRow = str(self.numIncompleteTasks + 2)
		self.incompleteTasksWorksheet.update_acell('A' + firstEmptyRow, newTask.name)
		self.incompleteTasksWorksheet.update_acell('B' + firstEmptyRow, self.numIncompleteTasks)
		self.incompleteTasksWorksheet.update_acell('C' + firstEmptyRow, newTask.type)
		self.incompleteTasksWorksheet.update_acell('D' + firstEmptyRow, newTask.priority)
		self.incompleteTasksWorksheet.update_acell('E' + firstEmptyRow, newTask.finishByDateTime)
		self.incompleteTasksWorksheet.update_acell('F' + firstEmptyRow, newTask.description)
		# possible bug here when the db gets updated but the numTasks is
			# not updated, will cause inconsitencies and that is rly bad
		self.numIncompleteTasks += 1

	def getFieldsFromDB(self):
		return self.incompleteTasksWorksheet.row_values(1)

	def getRecordsFromDB(self):
		ls = []
		for i in range(2, self.numIncompleteTasks+2):
			ls.append(self.incompleteTasksWorksheet.row_values(i))
		return ls

	def markTaskCompletedWithId(self, taskId):
		# copy the data in the specified row of the first sheet
		# use that data to create some sort of object to hold it?
		# then insert the data into the sheet containing completed tasks
		pass
