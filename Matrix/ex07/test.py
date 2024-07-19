from mathh import Matrix, Vector

def cross_product(u, v):
	if u.is_empty() or v.is_empty():
		raise ValueError("no empty vector")
	if u.shape != v.shape:
		raise ValueError("the 2 Vector must have the same shape")
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise ValueError("at least One of the argument is not Vector")
	if u.shape != v.shape:
		raise ValueError("Vector must have the same shape")
	if (u.shape[0] != 3 and u.shape[1] != 3) or (u.shape[0] == 3 and u.shape[1] == 3) :
		raise ValueError("wrong shape")
	 # Adapter le calcul en fonction de la forme des vecteurs
	if u.shape == (3, 1):  # Vecteur sous forme de colonne
		u1, u2, u3 = u.data[0][0], u.data[1][0], u.data[2][0]
		v1, v2, v3 = v.data[0][0], v.data[1][0], v.data[2][0]
		result = [
			[u2 * v3 - u3 * v2],
			[u3 * v1 - u1 * v3],
			[u1 * v2 - u2 * v1]
		]
	else:  # Vecteur sous forme de ligne
		u1, u2, u3 = u.data[0]
		v1, v2, v3 = v.data[0]
		result = [
			[u2 * v3 - u3 * v2, u3 * v1 - u1 * v3, u1 * v2 - u2 * v1],
		]

	return Vector(result)
def main():
	try :
		e1 = Vector([[4, 2]])
		e2 = Vector([[4], [2]])


		m1 = Matrix([[1., 0], [0, 1]])
		m2 = Matrix([[2,0], [0, 2]])
		m3 = Matrix([[2, -2], [-2, 2]])
		m4 = Matrix([[2, 1], [4,2]])
		m5 = Matrix([[3, -5], [6, 8]])

		e1 * m1
		m2 * e2
		m3 * e2
		m1 * m1
		m1 * m4
		m5 * m4


		# print("second test e2 :",cross_product(e8,e9))
		# print("third test e3 :",cross_product(e6,e7))

		# print("first error test m1 :",cross_product(m1,m1))
		# print("second error test m2 :",cross_product(e8,e9))

	
	except ValueError as e :
		print(e)		



if __name__ == "__main__":
	main()