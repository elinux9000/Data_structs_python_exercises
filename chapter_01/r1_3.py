'''Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''


def minmax(data):
	if not hasattr(type(data), '__iter__'):
		print("the function parameter must be a sequence type")
		raise TypeError
	min = max = data[0]
	for i in range(1, len(data)):
		if data[i] < min:
			min = data[i]
		if data[i] > max:
			max = data[i]
	return (min, max)
