# 時間を表す文字列 time から時と分を取得
#
# usage: split_time_str('123:15') -> (123, 15)
def split_time_str(time):
	hour, minute = time.split(':')
	return int(hour), int(minute)

# 時間を表す文字列 time が何分かを取得
#
# usage: get_minute_time_str('1:15') -> 75
def get_minute_time_str(time):
	hour, minute = split_time_str(time)
	return hour * 60 + minute

# 時と分から時間を表す文字列を生成する
#
# usage: generate_time_str(123, 5) -> '123:05'
def generate_time_str(hour, minute):
	return str(hour) + ':' + str(minute).zfill(2)

# 分表示を時間を表す文字列に変換
#
# usage: conv_minute_to_time(75) -> '1:15'
def conv_minute_to_time(minute):
	h = minute // 60
	m = minute % 60
	return generate_time_str(h, m)


# ある時間 x と y の和を求める
# x, y は H:mm の文字列
#
# usage: add_time('1:30', '0:10') -> '1:40'
def add_time(x, y):
	x_minute = get_minute_time_str(x)
	y_minute = get_minute_time_str(y)
	sum_minute = x_minute + y_minute
	sum_time = conv_minute_to_time(sum_minute)
	return sum_time

# ある時間 x と y の時間差を求める
# x, y は H:mm の文字列
#
# usage: sub_time('123:30', '1:10') -> '122:20'
#        sub_time('1:30', '2:15') -> '-0:45'
def sub_time(x, y):
	x_minute = get_minute_time_str(x)
	y_minute = get_minute_time_str(y)
	if x_minute >= y_minute:
		diff_minute = x_minute - y_minute
		is_negative = False
	else:
		diff_minute = y_minute - x_minute
		is_negative = True
	diff_time = conv_minute_to_time(diff_minute)
	if is_negative:
		diff_time = '-' + diff_time
	return diff_time

# ある時間 x を y で割った時間を求める
# x は H:mm の文字列, y は 数値
# 割り切れない場合は切り上げる
#
# usage: div_time('1:01', 3) -> '0:21'
def div_time(x, y):
	x_minute = get_minute_time_str(x)
	result = -(-x_minute // y)
	return conv_minute_to_time(result)

# ある時間 x と y を比較する
# x が大きい -> 正の数, y が大きい -> 負の数, x と y が同じ -> 0
def comp_time_str(x, y):
	x_minute = get_minute_time_str(x)
	y_minute = get_minute_time_str(y)
	return x_minute - y_minute
