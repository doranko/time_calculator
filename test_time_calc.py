import unittest
import time_calc as tc


class TestTashizan(unittest.TestCase):
	# 時間表記文字列を時間と分に分割
	# e.g. '123:45' -> (123, 45)
	def test_split_time_str(self):
		actual = tc.split_time_str('123:45')
		expected = 123, 45
		self.assertEqual(expected, actual)

	# 時間表記文字列を分に変換
	# e.g. '1:15' -> 75
	def test_get_minute_time_str(self):
		actual = tc.get_minute_time_str('1:15')
		expected = 75
		self.assertEqual(expected, actual)

	# 時間、分から時間表記文字列を生成
	# e.g. 123, 5 -> '123:05'
	def test_generate_time_str(self):
		actual = tc.generate_time_str(123, 5)
		expected = '123:05'
		self.assertEqual(expected, actual)

	# 分から時間表記文字列を生成
	# e.g. 75 -> '1:15'
	def test_conv_minute_to_time(self):
		actual = tc.conv_minute_to_time(75)
		expected = '1:15'
		self.assertEqual(expected, actual)

	# 時間表記文字列同士を足し算
	# e.g. '100:30' + '2:40' = '103:10'
	def test_add_time(self):
		actual = tc.add_time('100:30', '2:40')
		expected = '103:10'
		self.assertEqual(expected, actual)

	# 時間表記文字列同士を引き算
	# e.g. '100:30' - '2:40' = '97:50'
	def test_sub_time(self):
		actual = tc.sub_time('100:30', '2:40')
		expected = '97:50'
		self.assertEqual(expected, actual)
		# 引く時間の方が大きい場合は差分が負の数で返る
		actual = tc.sub_time('1:30', '2:15')
		expected = '-0:45'
		self.assertEqual(expected, actual)

	# 時間表記文字列を等分割
	# e.g. '1:01' / 3 = '0:21'
	def test_div_time(self):
		actual = tc.div_time('1:01', 3)
		expected = '0:21'
		self.assertEqual(expected, actual)

	# 時間表記文字列を比較
	# e.g. '1:00', '2:00' -> -1
	def test_comp_time_str(self):
		# 第一引数の方が大きい場合は正
		actual = tc.comp_time_str('1:00', '0:59')
		self.assertTrue(actual > 0)
		# 第二引数の方が大きい場合は負
		actual = tc.comp_time_str('0:59', '1:00')
		self.assertTrue(actual < 0)
		# どちらも同じ場合は 0
		actual = tc.comp_time_str('1:00', '1:00')
		self.assertEqual(0, actual)

if __name__ == "__main__":
	unittest.main()
