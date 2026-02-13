from mathh import Matrix, Vector

def main():
    print("Test 1: Trace of a 2x2 identity matrix")
    u = Matrix([[1., 0.], [0., 1.]])
    print(u.trace())  # Expected: 2.0

    print("\nTest 2: Trace of a 3x3 matrix")
    u = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
    print(u.trace())  # Expected: 9.0

    print("\nTest 3: Trace of another 3x3 matrix with negative values")
    u = Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]])
    print(u.trace())  # Expected: -21.0

    print("\nTest 4: Edge Case - Non-square matrix")
    try:
        u = Matrix([[1., 2., 3.], [4., 5., 6.]])
        print(u.trace())  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 5: Edge Case - Empty matrix")
    try:
        u = Matrix([])
        print(u.trace())  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 6: Trace of a large 4x4 matrix")
    u = Matrix([[1., 2., 3., 4.], [5., 6., 7., 8.], [9., 10., 11., 12.], [13., 14., 15., 16.]])
    print(u.trace())  # Expected: 34.0 (1 + 6 + 11 + 16)

    print("\nTest 7: Trace of a 5x5 identity matrix")
    u = Matrix([[1., 0., 0., 0., 0.], [0., 1., 0., 0., 0.], [0., 0., 1., 0., 0.], [0., 0., 0., 1., 0.], [0., 0., 0., 0., 1.]])
    print(u.trace())  # Expected: 5.0

if __name__ == "__main__":
    main()
