main objectives:

input will be a list of EVENTS, could come in a bunch or one at a time

input an event, without starvation, how do you schedule events?

event:
	description
	current time
	current date
	end time
	end date
	priority

schedule:  is a sorted list that contains events
schedule is a data struct that holds requeted events and has an order for you to do them in


	 mostUpToDateScheduleQueue



features:

benefits:




shit to do:
	create Event class
	do like a Console tyep input output class

	format the input so easy to input to program



	# import gspread
	# from oauth2client.service_account import ServiceAccountCredentials
	# from pprint import pprint
	#
	#
	# # all of this scheduling could be used in a console like thing or object to show things to user
	#
	# scope = ['https://www.googleapis.com/auth/drive']
	# serviceAccountCreds = ServiceAccountCredentials.from_json_keyfile_name('Scheduler-30eefa3a4c69.json', scope)
	# gc = gspread.authorize(serviceAccountCreds)
	# worksheet = gc.open('Scheduler').sheet1
	#
	# recordsInTable = worksheet.get_all_records()
	# # for x in recordsInTable:
	# pprint(recordsInTable)
	#
	#
	#
	# print()
	# print()
	# row = worksheet.row_values(3)
	# col = worksheet.col_values(1)
	# cellRaw = worksheet.cell(1,2)
	# cell = cellRaw.value
	#
	# rowToInsert = ["j", 25]
	# worksheet.insert_row(rowToInsert, 45)
	#
	#
	#
	# print(row)
	# print(col)
	# print(cellRaw)
	# print(cell)
	#
	# pprint(recordsInTable)
	#
	# # result = worksheet.spreadsheets().values().get(
	# #     spreadsheetId=sheet1, range=range_name).execute()
	# # numRows = result.get('values') if result.get('values')is not None else 0
	# # print('{0} rows retrieved.'.format(numRows))
	#
	#
	# # class DAO:
	# # 	def __init__(self):
	# # 		pass








i want to be able to input a task and have that task added to a queue of some kind

maybe a priortiy queue

how will i go about getting input from user, that should be a class, maybe

could also have routines which i can schedule on a custom basis

program will need to be able to manipulate database (will use gSheets for this)
	store tasks in the gSheets
	-> prob will need to

tasks(subject,
	priority,
	about line,
	currentTime,
	currentDate,
	expirationTime,

)

console(

)

scheduler(listOfTasks,

)

routine(listOfTasks,

)

		what would the mvp of this look like:
			it would be able to store something in the db and get that thing out at a different runtime




for now i think that is enough of a design

	-> create a new project on gSheets for this project
	-> link it to this project
	___
	at this point i think i need to work on the scheduler itself

	____________________________________________________________________________________________



	activities(duration,



	)
