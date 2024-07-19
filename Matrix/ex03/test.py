from ex07.mathh import Matrix, Vector


def main():
	try :
		e1 = Vector([[0., 0.]])
		e2 = Vector([[1., 1]])
		e3 = Vector([[1, 1.]])
		e4 = Vector([[1], [1]])
		e5 = Vector([[-1], [6], [0]])
		e6 = Vector([[3], [2], [1]])


		m1 = Matrix([[1., 2.], [3., 4.]])
		m2 = Matrix([[5.,6.], [7., 8.]])

		print(m1.dot(m2))
		print(e1.dot(e2))
		print(e2.dot(e3))
		print(e5.dot(e6))
		print(e4.dot(e5))

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()