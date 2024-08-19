from mathh import Matrix, Vector

def main():
    # Test de base avec des vecteurs
    print("Basic vector tests:")
    
    u = Vector([[0., 0.]])
    v = Vector([[1., 1.]])
    print(u.dot(v))  # Expected: 0.0

    u = Vector([[1., 1.]])
    v = Vector([[1., 1.]])
    print(u.dot(v))  # Expected: 2.0
    
    u = Vector([[-1., 6.]])
    v = Vector([[3., 2.]])
    print(u.dot(v))  # Expected: 9.0
    
    # Test avec des vecteurs de dimension plus élevée
    print("\nHigher dimension vector tests:")
    
    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(u.dot(v))  # Expected: 32.0 (1*4 + 2*5 + 3*6)
    
    u = Vector([[0., 1., 0.]])
    v = Vector([[0., 1., 0.]])
    print(u.dot(v))  # Expected: 1.0 (0*0 + 1*1 + 0*0)
    
    # Cas limite : Produit scalaire avec des vecteurs orthogonaux
    print("\nOrthogonal vectors:")
    
    u = Vector([[1., 0., 0.]])
    v = Vector([[0., 1., 0.]])
    print(u.dot(v))  # Expected: 0.0 (since they are orthogonal)
    
    # Cas limite : Produit scalaire avec des vecteurs de tailles différentes
    print("\nEdge case: Vectors of different sizes")
    try:
        u = Vector([[1., 2.]])
        v = Vector([[1., 2., 3.]])
        print(u.dot(v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)
    
    # Cas limite : Produit scalaire avec des vecteurs contenant des zéros
    print("\nEdge case: Vectors with zeros")
    
    u = Vector([[0., 0., 0.]])
    v = Vector([[0., 0., 0.]])
    print(u.dot(v))  # Expected: 0.0
    
    u = Vector([[0., 0., 1.]])
    v = Vector([[0., 1., 0.]])
    print(u.dot(v))  # Expected: 0.0
    
    # Cas limite : Produit scalaire avec des vecteurs négatifs
    print("\nEdge case: Vectors with negative values")
    
    u = Vector([[-1., -2., -3.]])
    v = Vector([[-4., -5., -6.]])
    print(u.dot(v))  # Expected: 32.0 (same as positive values)

if __name__ == "__main__":
    main()


# def main():
# 	try :
# 		e1 = Vector([[0., 0.]])
# 		e2 = Vector([[1., 1]])
# 		e3 = Vector([[1, 1.]])
# 		e4 = Vector([[1], [1]])
# 		e5 = Vector([[-1], [6], [0]])
# 		e6 = Vector([[3], [2], [1]])


# 		m1 = Matrix([[1., 2.], [3., 4.]])
# 		m2 = Matrix([[5.,6.], [7., 8.]])

# 		print(m1.dot(m2))
# 		print(e1.dot(e2))
# 		print(e2.dot(e3))
# 		print(e5.dot(e6))
# 		print(e4.dot(e5))

	
# 	except ValueError as e :
# 		print(e)		



# if __name__ == "__main__":
# 	main()