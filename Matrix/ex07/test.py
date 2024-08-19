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
    # Test 1: Multiplication d'un vecteur par un scalaire
    print("Test 1: Vector-Scalar Multiplication")
    v = Vector([[1, 2, 3]])
    print(v.mul_vec(3))  # Expected: [3, 6, 9]

    v = Vector([[0, -1, 2]])
    print(v.mul_vec(-2))  # Expected: [0, 2, -4]

    # Test 2: Produit scalaire entre deux vecteurs
    print("\nTest 2: Dot Product of Two Vectors")
    u = Vector([[1, 2, 3]])
    v = Vector([[4, 5, 6]])
    print(u.mul_vec(v))  # Expected: 32 (1*4 + 2*5 + 3*6)

    u = Vector([[0, 0, 0]])
    v = Vector([[1, 2, 3]])
    print(u.mul_vec(v))  # Expected: 0 (0*1 + 0*2 + 0*3)

    u = Vector([[1, 2, 3]])
    v = Vector([[-1, 0, 1]])
    print(u.mul_vec(v))  # Expected: 2 (1*(-1) + 2*0 + 3*1)

    # Test 3: Multiplication d'un vecteur par une matrice
    print("\nTest 3: Vector-Matrix Multiplication")
    u = Vector([[1, 2]])
    m = Matrix([[3, 4], [5, 6]])
    print(u.mul_vec(m))  # Expected: [13, 16] (1*3 + 2*5, 1*4 + 2*6)

    u = Vector([[1, 0]])
    m = Matrix([[7, 8], [9, 10]])
    print(u.mul_vec(m))  # Expected: [7, 8] (1*7 + 0*9, 1*8 + 0*10)

    u = Vector([[2, -1]])
    m = Matrix([[1, 0], [0, 1]])
    print(u.mul_vec(m))  # Expected: [2, -1] (2*1 + (-1)*0, 2*0 + (-1)*1)

    # Test 4: Cas limites avec vecteurs de tailles différentes pour produit scalaire
    print("\nTest 4: Edge Case - Vectors with Different Dimensions for Dot Product")
    try:
        u = Vector([[1, 2, 3]])
        v = Vector([[4, 5]])
        print(u.mul_vec(v))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    # Test 5: Multiplication d'un vecteur par un scalaire non valide (string)
    print("\nTest 5: Edge Case - Multiplication with Unsupported Type (string)")
    try:
        v = Vector([[1, 2, 3]])
        print(v * "invalid")  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    # Test 6: Multiplication d'un vecteur par une matrice incompatible
    print("\nTest 6: Edge Case - Incompatible Matrix-Vector Multiplication")
    try:
        u = Vector([[1, 2, 3]])
        m = Matrix([[1, 2], [3, 4]])
        print(u.mul_vec(m))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    # Test 7: Multiplication de vecteurs et matrices de grande dimension
    print("\nTest 7: Large Vectors and Matrices")
    u = Vector([[i for i in range(100)]])
    m = Matrix([[i + j for j in range(100)] for i in range(100)])
    result = u.mul_vec(m)
    print(f"Result for large vector and matrix multiplication (first 5 elements): {result.data[0][:5]}")

    # Test 8: Multiplication d'une matrice par un scalaire
    print("\nTest 8: Matrix-Scalar Multiplication")
    m = Matrix([[1, 2], [3, 4]])
    print(m.mul_mat(2))  # Expected: [[2, 4], [6, 8]]

    m = Matrix([[0, -1], [-2, 3]])
    print(m.mul_mat(-3))  # Expected: [[0, 3], [6, -9]]

    # Test 9: Cas limite - Vecteur vide
    print("\nTest 9: Edge Case - Empty Vector")
    try:
        v = Vector([])
        print(v.mul_vec(2))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    # Test 10: Cas limite - Matrice vide
    print("\nTest 10: Edge Case - Empty Matrix")
    try:
        m = Matrix([[]])
        v = Vector([[1, 2, 3]])
        print(m.mul_mat(v))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    # Test 11: Produit scalaire entre un vecteur et lui-même
    print("\nTest 11: Dot Product of Vector with Itself")
    u = Vector([[1, 2, 3]])
    print(u.mul_vec(u))  # Expected: 14 (1*1 + 2*2 + 3*3)

    # Test 12: Vecteur colonne et multiplication par une matrice compatible
    print("\nTest 12: Column Vector and Compatible Matrix Multiplication")
    u = Vector([[1], [2], [3]])
    m = Matrix([[4, 5, 6]])
    print(m.mul_mat(u))  # Expected: [32] (4*1 + 5*2 + 6*3)

    # Test 13: Produit scalaire entre deux vecteurs perpendiculaires
    print("\nTest 13: Dot Product of Perpendicular Vectors")
    u = Vector([[1, 0]])
    v = Vector([[0, 1]])
    print(u.mul_vec(v))  # Expected: 0 (since they are perpendicular)

if __name__ == "__main__":
    main()