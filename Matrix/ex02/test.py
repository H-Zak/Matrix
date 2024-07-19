from ex07.mathh import Matrix, Vector

def linear_interpolation(u, v, coefs):
	if v.shape != u.shape or not isinstance(coefs, (int, float)):
		raise ValueError("Vector have not the same shape or coefs is not a int or a float")
	shaping = u.shape

	if type(u) == Matrix:
		result = Matrix([[0.0 for _ in range(shaping[1])] for _ in range(shaping[0])])
	if type(u) == Vector:
		result = Vector([[0.0 for _ in range(shaping[1])] for _ in range(shaping[0])])
	inverse =  1 - coefs
	for i in range(shaping[0]):
			for j in range(shaping[1]):
					result.data[i][j] = round( u.data[i][j] * inverse + v.data[i][j] * coefs, 1)
	print(result)

		

def main():
	try :
		e1 = Vector([[2., 1.]])
		e2 = Vector([[4., 2]])
		e3 = Vector([[0., 0., 1.]])
		e4 = Vector([[1], [0], [0]])
		e5 = Vector([[0], [1], [0]])
		e6 = Vector([[0], [0], [1]])

		m1 = Matrix([[2., 1.], [3., 4.]])
		m2 = Matrix([[20.,10.], [30., 40.]])

		linear_interpolation(e1, e2, 0.3)
		linear_interpolation(m1,m2, 0.5)
	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()