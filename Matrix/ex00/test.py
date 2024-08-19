from mathh import Matrix, Vector


# faire tous les tests avec des tuples plutot que des lists


def main():
    # Test cases for Vector operations
    print("Testing Vector operations...")
    u = Vector([[2., 3.]])
    v = Vector([[5., 7.]])

    u = u + v
    print("u after addition:", u)  # Expected: [7.0, 10.0]

    u = Vector([[2., 3.]])
    v = Vector([[5., 7.]])

    u = u - v
    print("u after subtraction:", u)  # Expected: [-3.0, -4.0]

    u = Vector([[2., 3.]])
    u = u * 2
    print("u after scaling:", u)  # Expected: [4.0, 6.0]

    # Test cases for Matrix operations
    print("\nTesting Matrix operations...")
    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    v = Matrix([
        [7., 4.],
        [-2., 2.]
    ])

    u = u + v
    print("u after addition:\n", u)  # Expected: [8.0, 6.0] [1.0, 6.0]

    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    v = Matrix([
        [7., 4.],
        [-2., 2.]
    ])

    u = u - v
    print("u after subtraction:\n", u)  # Expected: [-6.0, -2.0] [5.0, 2.0]

    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    u = 2 * u
    print("u after scaling:\n", u)  # Expected: [2.0, 4.0] [6.0, 8.0]

    # Edge case tests
    print("\nTesting edge cases...")
    try:
        u = Vector([1., 2., 3.])
        v = Vector([4., 5.])
        u = u + v  # This should raise an error
    except ValueError as e:
        print("Caught an error for vectors of different sizes:", e)

    try:
        u = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        v = Matrix([
            [1., 2., 3.],
            [4., 5., 6.]
        ])
        u = u + v  # This should raise an error
    except ValueError as e:
        print("Caught an error for matrices of different sizes:", e)

    try:
        u = Matrix([
            [1., 2.],
            [3., 4., 5.]  # Cette ligne a 3 éléments, contrairement à la première ligne qui en a 2
        ])
        print("Test failed: Matrix with rows of different lengths was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for matrix with rows of different lengths:", e)
    try:
        u = Matrix([])  # Matrice vide
        print("Test failed: Empty matrix was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for empty matrix:", e)

    try:
        u = Matrix([
            [1., 2.],
            []  # Ligne vide
        ])
        print("Test failed: Matrix with an empty row was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for matrix with an empty row:", e)

    try:
        u = Matrix([
            [1., 2.],
            [3., "a"]  # Un élément n'est pas un nombre
        ])
        print("Test failed: Matrix with non-numeric elements was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for matrix with non-numeric elements:", e)


    try:
        u = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        v = Matrix([
            [1., 2., 3.],  # Matrice de taille 2x3
            [4., 5., 6.]
        ])
        u.add(v)  # Les matrices n'ont pas les mêmes dimensions
        print("Test failed: Addition of matrices with different sizes was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for addition of matrices with different sizes:", e)

    try:
        u = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        v = Matrix([
            [1., 2.],  # Matrice de taille 1x2
        ])
        u.sub(v)  # Les matrices n'ont pas les mêmes dimensions
        print("Test failed: Subtraction of matrices with different sizes was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for subtraction of matrices with different sizes:", e)


    try:
        u = Matrix([
            [1., 2., 3.],
            [4., 5., 6.]
        ])
        u.inverse()  # Si la fonction inverse est définie, elle devrait échouer pour une matrice non carrée
        print("Test failed: Inversion of a non-square matrix was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for inversion of a non-square matrix:", e)

    try:
        u = Matrix([
            [1., 2.],
            [{"key": "value"}, 3.]  # Un élément est un dictionnaire
        ])
        print("Test failed: Matrix with complex objects was accepted.")
    except ValueError as e:
        print("Test passed: Caught an error for matrix with complex objects:", e)




    
if __name__ == "__main__":
    main()
