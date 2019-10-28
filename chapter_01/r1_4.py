def sum_squares(n):
	sum = 0
	step = 1
	if n < 0:
		step = -1
	for i in range(0, n, step):
		sum += i * i

	return sum
