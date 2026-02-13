from mathh import Matrix, Vector

def main():
    print("Test 1: Inverse of a 3x3 Identity Matrix")
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]
    ])
    print("Matrix:\n", u)
    print("Inverse:\n", u.inverse())  # Expected: Identity matrix

    print("\nTest 2: Inverse of a 3x3 Diagonal Matrix")
    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.]
    ])
    print("Matrix:\n", u)
    print("Inverse:\n", u.inverse())  # Expected: Diagonal matrix with 0.5

    print("\nTest 3: Inverse of a 3x3 Generic Matrix")
    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.]
    ])
    print("Matrix:\n", u)
    print("Inverse:\n", u.inverse())
    # Expected:
    # [0.649425287, 0.097701149, -0.655172414]
    # [-0.781609195, -0.126436782, 0.965517241]
    # [0.143678161, 0.074712644, -0.206896552]


    print("\nTest 4: Edge Case - Singular Matrix")
    try:
        u = Matrix([
            [1., 2., 3.],
            [4., 5., 6.],
            [7., 8., 9.]
        ])
        print("Matrix:\n", u)
        print("Inverse:\n", u.inverse())  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 5: Edge Case - Non-square Matrix")
    try:
        u = Matrix([
            [1., 2., 3.],
            [4., 5., 6.]
        ])
        print("Matrix:\n", u)
        print("Inverse:\n", u.inverse())  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 6: Validation A⁻¹A = I - Singular Matrix Test")
    try:
        u = Matrix([
            [1., 2., 3., 4., 5.],
            [1., 2., 3., 4., 5.],  # ligne dupliquée -> singulière
            [0., 1., 0., 0., 0.],
            [0., 0., 1., 0., 0.],
            [0., 0., 0., 1., 0.],
        ])
        print("Matrix:\n", u)
        print("Inverse:\n", u.inverse())  # doit lever ValueError("Singular Matrix")
    except ValueError as e:
        print("Caught an error as expected:", e)

if __name__ == "__main__":
    main()
