from ex07.mathh import Matrix, Vector


# faire tous les tests avec des tuples plutot que des lists

def main():
	try :
		m1 = Matrix([[1, 2]])
		m2 = Matrix([[-1, 0], [-2, 5]])
		v1 = Vector([[1, 2]])
		# import pdb; pdb.set_trace()
		v2 = Vector([[-1, 8]])
		
		# v3 = Vector([[-1, 0], [-2, 5]])
		# print(str(m))
		# m2 = Matrix([[-1.0, -2.0], [-3.0, -4.0]])
		# m3 = Vector([[1.0], [2.0]])
		# m3 = Vector([[1.0], [2.0]])
		# result = m1 * m2
		# print(result)
		# result = m1 + m2
		# print(result)
		# result = m1 - m2
		# print(result)
		# result = m1 / 2
		# print(result)
		# result = m1 * 2
		# print(result)


		result = 2 - v1
		# print(result)
		# result = v1 + v2
		# print(result)
		# result = v1 - v2
		# print(result)
		# result = v1 / 2
		# print(result)
		# result = v1 * 2
		# print(result)


	except ValueError as e :
		print(e)

		
if __name__ == "__main__":
	main()
