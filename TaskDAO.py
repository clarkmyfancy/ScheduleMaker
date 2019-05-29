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
		self.worksheet = self.gc.open('taskDB').sheet1

	def updateDBWithTask(self, newTask):
		numTasks = len(self.worksheet.col_values(1)) - 1
		firstEmptyRow = str(numTasks + 2)
		self.worksheet.update_acell('A' + firstEmptyRow, newTask.name)
		self.worksheet.update_acell('B' + firstEmptyRow, numTasks)
		self.worksheet.update_acell('C' + firstEmptyRow, newTask.type)
		self.worksheet.update_acell('D' + firstEmptyRow, newTask.priority)
		self.worksheet.update_acell('E' + firstEmptyRow, newTask.finishByDateTime)
		self.worksheet.update_acell('F' + firstEmptyRow, newTask.description)
