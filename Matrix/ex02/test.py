from mathh import Matrix, Vector

def lerp(u, v, t):
	if not (0 <= t <= 1):
		raise ValueError("The interpolation factor t must be between 0 and 1.")
	if isinstance(u, (int, float)) and isinstance(v, (int, float)):
		return u * (1 - t) + v * t
	if v.shape != u.shape or not isinstance(t, (int, float)):
		raise ValueError("Vector have not the same shape or t is not a int or a float")
	shaping = u.shape

	if type(u) == Matrix:
		result = Matrix([[0.0 for _ in range(shaping[1])] for _ in range(shaping[0])])
	if type(u) == Vector:
		result = Vector([[0.0 for _ in range(shaping[1])] for _ in range(shaping[0])])
	inverse =  1 - t
	for i in range(shaping[0]):
			for j in range(shaping[1]):
					result.data[i][j] = round( u.data[i][j] * inverse + v.data[i][j] * t, 1)
	return result

		

def main():
    # Test de base avec des nombres
    print("Basic number tests:")
    print(lerp(0., 1., 0.))  # Expected: 0.0
    print(lerp(0., 1., 1.))  # Expected: 1.0
    print(lerp(0., 1., 0.5))  # Expected: 0.5
    print(lerp(21., 42., 0.3))  # Expected: 27.3
    
    # Test avec des Vecteurs
    print("\nVector tests:")
    v1 = Vector([[2., 1.]])
    v2 = Vector([[4., 2.]])
    print(lerp(v1, v2, 0.3))  # Expected: [2.6, 1.3]
    
    v3 = Vector([[0., 0.]])
    v4 = Vector([[10., 10.]])
    print(lerp(v3, v4, 0.5))  # Expected: [5.0, 5.0]
    
    # Test avec des Matrices
    print("\nMatrix tests:")
    m1 = Matrix([
        [2., 1.],
        [3., 4.]
    ])
    m2 = Matrix([
        [20., 10.],
        [30., 40.]
    ])
    print(lerp(m1, m2, 0.5))  # Expected: [[11.0, 5.5], [16.5, 22.0]]
    
    m3 = Matrix([
        [0., 0.],
        [0., 0.]
    ])
    m4 = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    print(lerp(m3, m4, 1.0))  # Expected: [[1.0, 2.0], [3.0, 4.0]]
    
    # Cas limite : Facteur d'interpolation en dehors de [0, 1]
    print("\nEdge case: t out of bounds")
    try:
        print(lerp(0., 1., 1.5))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)
    
    # Cas limite : Vecteurs de tailles différentes
    print("\nEdge case: Vectors of different sizes")
    try:
        v5 = Vector([[1., 2.]])
        v6 = Vector([[1., 2., 3.]])
        print(lerp(v5, v6, 0.5))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)
    
    # Cas limite : Matrices de tailles différentes
    print("\nEdge case: Matrices of different sizes")
    try:
        m5 = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        m6 = Matrix([
            [1., 2., 3.],
            [4., 5., 6.]
        ])
        print(lerp(m5, m6, 0.5))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)

if __name__ == "__main__":
    main()
