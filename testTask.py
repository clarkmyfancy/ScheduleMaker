import unittest
import Task as t

class TestTask(unittest.TestCase):

	def setUp(self):
		self.t1 = t.Task("wash clothes", "chore", 0, "2018-29-5 12:30:00")
		self.t2 = t.Task("clean dishes", "chore", 0, "2018-29-5 14:30:00", "make sure to handwash the chefs knife")

	def tearDown(self):
		del self.t1
		del self.t2

	def test_task_t1(self):
		print("t1 test")
		self.assertEquals(self.t1.name, "wash clothes")
		self.assertEquals(self.t1.id, 0)
		self.assertEquals(self.t1.type, "chore")
		self.assertEquals(self.t1.priority, 0)
		self.assertEquals(self.t1.finishByDateTime, "2018-29-5 12:30:00")
		self.assertIsNone(self.t1.description)

	def test_task_t2(self):
		print("t2 test")
		self.assertEquals(self.t2.name, "clean dishes")
		self.assertEquals(self.t2.id, 1)
		self.assertEquals(self.t2.type, "chore")
		self.assertEquals(self.t2.priority, 0)
		self.assertEquals(self.t2.finishByDateTime, "2018-29-5 14:30:00")
		self.assertIsNotNone(self.t2.description)
