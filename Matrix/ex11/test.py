from mathh import Matrix, Vector


def main():
    # Test 1: Déterminant d'une matrice 1x1
    print("Test 1: Determinant of a 1x1 Matrix")
    u = Matrix([[5.]])
    print("Matrix:\n", u)
    print("Determinant:", u.determinant())  # Expected: 5.0

    # Test 2: Déterminant d'une matrice 2x2
    print("\nTest 2: Determinant of a 2x2 Matrix")
    u = Matrix([[1., -1.], [-1., 1.]])
    print("Matrix:\n", u)
    print("Determinant:", u.determinant())  # Expected: 0.0

    # Test 3: Déterminant d'une matrice 3x3
    print("\nTest 3: Determinant of a 3x3 Matrix")
    u = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
    print("Matrix:\n", u)
    print("Determinant:", u.determinant())  # Expected: -174.0

    # Test 4: Déterminant d'une matrice 4x4
    print("\nTest 4: Determinant of a 4x4 Matrix")
    u = Matrix([
        [8., 5., -2., 4.],
        [4., 2.5, 20., 4.],
        [8., 5., 1., 4.],
        [28., -4., 17., 1.]
    ])
    print("Matrix:\n", u)
    print("Determinant:", u.determinant())  # Expected: 1032.0

    # Test 5: Cas limite - Matrice non carrée
    print("\nTest 5: Edge Case - Non-square matrix")
    try:
        u = Matrix([[1., 2., 3.], [4., 5., 6.]])
        print("Matrix:\n", u)
        print("Determinant:", u.determinant())  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    # Test 6: Cas limite - Matrice 2x2 avec des zéros
    print("\nTest 6: Edge Case - 2x2 Matrix with Zeros")
    u = Matrix([[0., 0.], [0., 0.]])
    print("Matrix:\n", u)
    print("Determinant:", u.determinant())  # Expected: 0.0

if __name__ == "__main__":
    main()
