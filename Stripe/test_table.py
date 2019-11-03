import unittest
from table import DataBase

class TestDB(unittest.TestCase):
	def test_min_by_column(self):
		test_cases = [([{"a": 1},{"a": 2},{"a": 3}], 'a', {"a": 1}),
					  ([{"a": 1}], 'a', [])
					]
		data_base = DataBase()
		for i, triplet in enumerate(test_cases):
			table, target, expected = triplet
			actual = data_base.min_by_column(table, target)
			assert actual == expected, 'Fail on test case ' + str(i + 1)
		print('Passed all test cases')

if __name__ == '__main__':
	test_database = TestDB()
	test_database.test_min_by_column()