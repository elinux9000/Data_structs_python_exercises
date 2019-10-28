def is_multiple(n, m):
	#Write a short python function is_multiple(n,m) that takes 2 integer values and returns True if n is a multiple of m and False otherse
	int_type = type(1)
	if type(n) != int_type or type(m) != int_type:
		raise TypeError
	if n % m == 0:
		return True
	return False


if __name__ == "__main__":
	n = [1, 4, 3, 7, 10, 100, -8, 12, 12.1]
	m = [1, 2, 3, 4, 5, 25, 4, -4, .1]
	answers = [True, True, True, False, True, True, True, True, True, False]
	for i in range(len(n)):
		if (multiple(n[i], m[i]) == answers[i]):
			print("Test ", i, "passed")
		else:
			print("Test", i, "failed")
			raise SystemExit
