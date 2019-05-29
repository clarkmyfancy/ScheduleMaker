class Task:

	NextTaskId = 0

	def __init__(self, _name, _type, _priority, _finishByDateTime, _description=None):
		self.name = _name
		self.id = Task.NextTaskId
		Task.NextTaskId += 1
		self.type = _type
		self.priority = _priority
		self.finishByDateTime = _finishByDateTime
		self.description = _description

	def __del__(self):
		Task.NextTaskId -= 1
