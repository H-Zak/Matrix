from mathh import Matrix, Vector

def main():
    print("Test 1: Row-Echelon Form of a 3x3 Identity Matrix")
    u = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 0.0 0.0
    # 0.0 1.0 0.0
    # 0.0 0.0 1.0

    print("\nTest 2: Row-Echelon Form of a 2x2 Matrix")
    u = Matrix([[1., 2.], [3., 4.]])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 0.0
    # 0.0 1.0

    print("\nTest 3: Row-Echelon Form of a Matrix with a Proportional Row")
    u = Matrix([[1., 2.], [2., 4.]])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 2.0
    # 0.0 0.0

    print("\nTest 4: Row-Echelon Form of a 3x5 Matrix")
    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
    ])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 0.62500000 0.0 0.0 -12.16666667
    # 0.0 0.0 1.0 0.0 -3.66666667
    # 0.0 0.0 0.0 1.0 29.5

    print("\nTest 5: Edge Case - Matrix with Leading Zeros")
    u = Matrix([[0., 2., 3.], [0., 0., 1.], [1., 2., 3.]])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 2.0 3.0
    # 0.0 1.0 1.5
    # 0.0 0.0 1.0

    print("\nTest 6: Edge Case - Empty Matrix")
    u = Matrix([])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected: Should return an empty matrix

    print("\nTest 7: Edge Case - Matrix with Zero Row")
    u = Matrix([[1., 2., 3.], [0., 0., 0.], [4., 5., 6.]])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 2.0 3.0
    # 0.0 1.0 1.5
    # 0.0 0.0 0.0

    print("\nTest 8: ")
    u = Matrix([[8., 5., -2., 4, 28], [4., 2.5, 20., 4,-4], [ 8., 5., 1., 4,17]])
    print("Original Matrix:\n", u)
    print("Row-Echelon Form:\n", u.row_echelon())
    # Expected:
    # 1.0 2.0 3.0
    # 0.0 1.0 1.5
    # 0.0 0.0 0.0

if __name__ == "__main__":
    main()
