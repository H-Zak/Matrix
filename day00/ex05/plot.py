import numpy as np
import matplotlib.pyplot as plt
from prediction import predict_




def plto(x, y, theta):
	"""Plot the data and prediction line from three non-empty numpy.array. Args:
      x: has to be an numpy.array, a one-dimensional array of size m.
      y: has to be an numpy.array, a one-dimensional array of size m.
      theta: has to be an numpy.array, a two-dimensional array of shape 2 * 1.
    Returns:
        Nothing.
    Raises:
      This function should not raise any Exceptions.
	"""
	if not isinstance(y, np.ndarray) or not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
		return None
	if x.ndim != 1 or y.ndim != 1 or x.size != y.size:
		return None
	row, col = theta.shape
	if row != 2 or col != 1:
		return None
	prediction = predict_(x, theta)
	plt.scatter(x , y, color='blue', label='Data points')

	plt.plot(x, prediction, color='red', label='Prediction line')
	  # Ajouter des légendes et titres
	plt.title('Data and Prediction Line')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.show()


def main():
	x = np.arange(1,6)
	y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
	# Example 1:
	theta1 = np.array([[4.5],[-0.2]])
	plto(x,y,theta1)
	theta2 = np.array([[-1.5],[2]])
	plto(x, y, theta2)
	theta3 = np.array([[3],[0.3]])
	plto(x, y, theta3)

if __name__ =="__main__":
	main()




