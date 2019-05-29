import unittest
# import Schedule as sch
import queue as _queue
import TaskOrderer as sch

class TestTaskOrderer(unittest.TestCase):

	def setUp(self):
		self.s = sch.TaskOrderer()


	def tearDown(self):
		del self.s


	def test_e(self):
		self.assertEquals(self.s.returnCurrentSchedule(), [])

	def test_insertEventIntoQueue(self):
		blankQueue = _queue.PriorityQueue()
		self.assertEquals(self.s.insertEventIntoQueue("event 1", blankQueue), ["event 1"])
