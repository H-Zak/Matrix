import numpy as np






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


def predict_(x, theta):
	"""Computes the vector of prediction y_hat from two non-empty numpy.array. Args:
		x: has to be an numpy.array, a one-dimensional array of size m.
		theta: has to be an numpy.array, a two-dimensional array of shape 2 * 1.
		Returns:
		y_hat as a numpy.array, a two-dimensional array of shape m * 1.
		None if x and/or theta are not numpy.array.
		None if x or theta are empty numpy.array.
		None if x or theta dimensions are not appropriate.
		Raises:
		This function should not raise any Exceptions.
	"""
	if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
		return None
	if x.size == 0 or theta.size == 0:
		return None
	row, col = theta.shape
	if row != 2 and col != 1 :
		return None
	y = add_intercept(x)
	prediction = y @ theta
	return prediction

def main():
	x = np.arange(1,6)
	# Example 1:
	theta1 = np.array([[5], [0]])
	print(predict_(x, theta1))

	theta2 = np.array([[0], [1]])
	print(predict_(x, theta2))

	theta3 = np.array([[5], [3]])
	print(predict_(x, theta3))

	theta4 = np.array([[-3], [1]])
	print(predict_(x, theta4))

if __name__ == "__main__":
	main()
