import numpy as np

def main():
	x = np.arange(1,6)
	print(add_intercept(x))
	y = np.arange(1,10).reshape((3,3))
	print(add_intercept(y))

def add_intercept(x):
	"""Adds a column of 1’s to the non-empty numpy.array x. Args:
		x: has to be a numpy.array. x can be a one-dimensional (m * 1) or two-dimensional (m * n) array.
		Returns:
		X, a numpy.array of dimension m * (n + 1).
		None if x is not a numpy.array.
		None if x is an empty numpy.array.
		Raises:
		This function should not raise any Exception.
	"""
	if not isinstance(x, np.ndarray) or x.size == 0:
		return None
	if x.ndim == 1:
		x = x.reshape(-1,1)
	m = x.shape[0]
	ones = np.ones((m,1))
	return np.hstack((ones, x))


if __name__ == "__main__":
	main()
