from ex07.mathh import Matrix, Vector

def cos(u, v):
	if u.is_empty() or v.is_empty():
		raise ValueError("no empty vector")
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise ValueError("One of the argument is not Vector")
	if u.shape != v.shape:
		raise ValueError("Vector must have the same shape")
	cos = u.dot(v) / (u.norm_2() * v.norm_2())
	return round(cos, 9)
def main():
	try :
		e1 = Vector([[1, 0]])
		e2 = Vector([[0, 1]])
		e3 = Vector([[0, 1]])
		e4 = Vector([[-1], [1]])
		e5 = Vector([[1], [-1]])
		e6 = Vector([[2], [1]])
		e7 = Vector([[4], [2]])
		e8 = Vector([[1], [2],[3]])
		e9 = Vector([[4], [5], [6]])


		m1 = Matrix([[1., 2.], [3., 4.]])
		m2 = Matrix([[5.,6.], [7., 8.]])

		print("first test e1 :",cos(e1,e1))
		print("second test e2 :",cos(e1,e2))
		print("third test e3 :",cos(e4,e5))

		print("first error test m1 :",cos(e6,e7))
		print("second error test m2 :",cos(e8,e9))

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()