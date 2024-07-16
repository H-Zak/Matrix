from matrix import Matrix, Vector


def main():
	try :
		m = Matrix([[1, 2],
			  [3, 4]])
		print(str(m))
		# m2 = Matrix([[-1.0, -2.0], [-3.0, -4.0]])
		# m3 = Vector([[1.0], [2.0]])
		# m3 = Vector([[1.0], [2.0]])
		# m * m3
		# print(type(m3) , type(m2), "\n")
		# m * m
		# m + [[1.0, 2.0], [3.0, 4.0]]
		# [[1.0, 2.0], [3.0, 4.0]] + m

		# m - m2
		# m2 - m
		# type(2)
		# m / 2
		# 2 / m
	except ValueError as e :
		print(e)
if __name__ == "__main__":
	main()
