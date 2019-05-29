import unittest

loader = unittest.TestLoader()
runner = unittest.TextTestRunner()

start_dir = '/Users/clarkmyfancy/Desktop/stuffIMake/software/python/Schedule'
suite = loader.discover(start_dir)
runner.run(suite)
