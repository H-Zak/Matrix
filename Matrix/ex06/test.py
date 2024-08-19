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
    # Test de base avec des vecteurs unitaires
    print("Basic tests with unit vectors:")
    
    u = Vector([[0., 0., 1.]])
    v = Vector([[1., 0., 0.]])
    print(cross_product(u,v))  # Expected: [0., 1., 0.]

    # Test avec des vecteurs non unitaires
    print("\nTests with non-unit vectors:")
    
    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(cross_product(u,v))  # Expected: [-3., 6., -3.]
    
    u = Vector([[4., 2., -3.]])
    v = Vector([[-2., -5., 16.]])
    print(cross_product(u,v))  # Expected: [17., -58., -16.]
    
    # Cas limite : Produit vectoriel d'un vecteur avec lui-même
    print("\nEdge case: Cross product of a vector with itself")
    
    u = Vector([[1., 2., 3.]])
    print(cross_product(u, u))  # Expected: [0., 0., 0.] (since the cross product with itself should be zero)
    
    # Cas limite : Vecteurs de dimensions différentes
    print("\nEdge case: Vectors of different sizes")
    try:
        u = Vector([[1., 2., 3.]])
        v = Vector([[1., 2.]])
        print(cross_product(u,v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)
    
    # Cas limite : Vecteurs avec des composants nuls
    print("\nEdge case: Vectors with zero components")
    
    u = Vector([[1., 0., 0.]])
    v = Vector([[0., 1., 0.]])
    print(cross_product(u,v))  # Expected: [0., 0., 1.]
    
    u = Vector([[0., 1., 0.]])
    v = Vector([[0., 0., 1.]])
    print(cross_product(u,v))  # Expected: [1., 0., 0.]

if __name__ == "__main__":
    main()