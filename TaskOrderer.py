
import queue as _queue

class TaskOrderer:

	def __init__(self):
		self.schedule = []


	def returnCurrentSchedule(self):
		return self.schedule

	def addEventToList(self, event, list):
		''' if going through and converting thier priority and such
		into a single number, the function will map and event and its priorities to
		 one number

		the task associated with that number will then be queued in decreasing TaskOrderer
		'''
		pass

	def insertEventIntoQueue(self, event, q = None):
		if q is None:
			q = _queue.PriorityQueue()
		q.put(event)

		contents = []
		while not q.empty():
			thing = q.get()
			print(thing)
			contents.append(thing)
		return contents
