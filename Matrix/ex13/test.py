from mathh import Matrix, Vector


def main():
    print("Test 1: Rank of a 3x3 Identity Matrix")
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])
    print("Matrix:\n", u)
    print("Rank:", u.rank())  # Expected: 3

    print("\nTest 2: Rank of a 4x4 Matrix with Dependent Columns")
    u = Matrix([
        [1., 2., 0., 0.],
        [2., 4., 0., 0.],
        [-1., 2., 1., 1.],
        [0., 0., 0., 0.]
    ])

    print("Matrix:\n", u)
    print("Rank:", u.rank())  # Expected: 2

    print("\nTest 3: Rank of a 4x3 Generic Matrix")
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
        [21., 18., 7.]
    ])
    print("Matrix:\n", u)
    print("Rank:", u.rank())  # Expected: 3

    print("\nTest 4: Edge Case - Rank of a 3x3 Zero Matrix")
    u = Matrix([
        [0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]
    ])
    print("Matrix:\n", u)
    print("Rank:", u.rank())  # Expected: 0

    print("\nTest 5: Rank of a 2x3 Matrix with a Zero Row")
    u = Matrix([
        [1., 2., 3.],
        [0., 0., 0.]
    ])
    print("Matrix:\n", u)
    print("Rank:", u.rank())  # Expected: 1

if __name__ == "__main__":
    main()

