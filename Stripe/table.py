import unittest

class DataBase(object):
	def exist_table(self, table):
		return False if not table else True

	def has_type_int(self, num):
		return True if type(num) == type(0) else False

	def min_by_column(self, table, col_name):
		if not self.exist_table(table):
			return []
		ans, min_val = table[0], float('inf')
		for row in table:
			row_value = row.get(col_name, 0)
			if not self.has_type_int(row_value):
				row_value = 0
			if row_value < min_val:
				min_val, ans = row_value, row
		return ans


# class TestDB(unittest.TestCase):
# 	def test_min_by_column(self):
# 		test_cases = [([{"a": 1},{"a": 2},{"a": 3}], 'a', {"a": 1}),
# 					  ([], 'a', [])
# 					]
# 		data_base = DataBase()
# 		for i, triplet in enumerate(test_cases):
# 			table, target, expected = triplet
# 			actual = data_base.min_by_column(table, target)
# 			assert actual == expected, 'Fail on test case ' + str(i + 1)
# 		print('Passed all test cases')

# if __name__ == '__main__':
# 	test_database = TestDB()
# 	test_database.test_min_by_column()