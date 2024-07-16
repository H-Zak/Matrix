import numpy as np

def main():
	x = np.arange(1,6)
	theta1 = np.array([5, 0])
	print(prediction(x, theta1))

	theta2 = np.array([0, 1])
	print(prediction(x,theta2))
	theta3 = np.array([5, 3])
	print(prediction(x , theta3))
	theta4 = np.array([-3, 1])
	print(prediction(x, theta4))

def prediction(x, teta):
	if not isinstance(x, (np.ndarray)) or not isinstance(teta, (np.ndarray)) :
		print(1)
		return None
	if len(teta.shape) != 1 or teta.size == 0:
		print(2)
		return None
	if len(x.shape) != 1 or x.size == 0:
		print(3)
		return None
	prediction = [int(teta[0] + teta[1] * x1) for x1 in x]

	return prediction

if __name__ == "__main__":
	main()


