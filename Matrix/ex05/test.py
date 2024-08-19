from mathh import Matrix, Vector

def angle_cos(u, v):
	if u.is_empty() or v.is_empty():
		raise ValueError("no empty vector")
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise ValueError("One of the argument is not Vector")
	if u.shape != v.shape:
		raise ValueError("Vector must have the same shape")
	if u.norm_2() == 0 or v.norm_2() == 0:
		raise ValueError("cannot divide by 0")
	cos = u.dot(v) / (u.norm_2() * v.norm_2())
	return round(cos, 9)


def main():
    # Test de base avec des vecteurs identiques
    print("Basic tests with identical vectors:")
    
    u = Vector([[1., 0.]])
    v = Vector([[1., 0.]])
    print(angle_cos(u, v))  # Expected: 1.0

    # Test avec des vecteurs orthogonaux
    print("\nBasic tests with orthogonal vectors:")
    
    u = Vector([[1., 0.]])
    v = Vector([[0., 1.]])
    print(angle_cos(u, v))  # Expected: 0.0
    
    # Test avec des vecteurs opposés
    print("\nBasic tests with opposite vectors:")
    
    u = Vector([[-1., 1.]])
    v = Vector([[1., -1.]])
    print(angle_cos(u,v))  # Expected: -1.0
    
    # Test avec des vecteurs colinéaires
    print("\nBasic tests with collinear vectors:")
    
    u = Vector([[2., 1.]])
    v = Vector([[4., 2.]])
    print(angle_cos(u,v))  # Expected: 1.0
    
    # Test avec des vecteurs de plus grande dimension
    print("\nTests with higher dimension vectors:")
    
    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(angle_cos(u,v))  # Expected: 0.974631846
    
    # Cas limite : Vecteurs de tailles différentes
    print("\nEdge case: Vectors of different sizes")
    try:
        u = Vector([[1., 2.]])
        v = Vector([[1., 2., 3.]])
        print(angle_cos(u ,v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)
    
    # Cas limite : Vecteurs nuls
    print("\nEdge case: Zero vectors")
    try:
        u = Vector([[0., 0.]])
        v = Vector([[1., 1.]])
        print(angle_cos(u, v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)
    
    try:
        u = Vector([[0., 0.]])
        v = Vector([[0., 0.]])
        print(angle_cos(u, v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)

if __name__ == "__main__":
    main()
    
# def main():
# 	try :
# 		e1 = Vector([[1, 0]])
# 		e2 = Vector([[0, 1]])
# 		e3 = Vector([[0, 1]])
# 		e4 = Vector([[-1], [1]])
# 		e5 = Vector([[1], [-1]])
# 		e6 = Vector([[2], [1]])
# 		e7 = Vector([[4], [2]])
# 		e8 = Vector([[1], [2],[3]])
# 		e9 = Vector([[4], [5], [6]])


# 		m1 = Matrix([[1., 2.], [3., 4.]])
# 		m2 = Matrix([[5.,6.], [7., 8.]])

# 		print("first test e1 :",cos(e1,e1))
# 		print("second test e2 :",cos(e1,e2))
# 		print("third test e3 :",cos(e4,e5))

# 		print("first error test m1 :",cos(e6,e7))
# 		print("second error test m2 :",cos(e8,e9))

	
# 	except ValueError as e :
# 		print(e)		



# if __name__ == "__main__":
# 	main()