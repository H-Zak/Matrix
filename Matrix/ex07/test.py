from mathh import Matrix, Vector, cross_product
def main():
    print("Test 1: Vector-Scalar Multiplication")
    v = Vector([[1, 2, 3]])
    print(v.mul_vec(3))  # Expected: [3, 6, 9]

    v = Vector([[0, -1, 2]])
    print(v.mul_vec(-2))  # Expected: [0, 2, -4]

    print("\nTest 2: Dot Product of Two Vectors")
    u = Vector([[1, 2, 3]])
    v = Vector([[4, 5, 6]])
    print(u.mul_vec(v))  # Expected: 32 (1*4 + 2*5 + 3*6)

    u = Vector([[0, 0, 0]])
    v = Vector([[1, 2, 3]])
    print(u.mul_vec(v))  # Expected: 0 (0*1 + 0*2 + 0*3)

    u = Vector([[1, 2, 3]])
    v = Vector([[-1, 0, 1]])
    print(u.mul_vec(v))  # Expected: 2 (1*(-1) + 2*0 + 3*1)

    print("\nTest 3: Matrix-Vector Multiplication")
    u = Vector([[1, 2]])
    m = Matrix([[3, 4], [5, 6]])
    print(m.mul_vec(u))  # Expected: [13, 16] (1*3 + 2*5, 1*4 + 2*6)

    u = Vector([[1, 0]])
    m = Matrix([[7, 8], [9, 10]])
    print(m.mul_vec(u))  # Expected: [7, 8] (1*7 + 0*9, 1*8 + 0*10)

    u = Vector([[2, -1]])
    m = Matrix([[1, 0], [0, 1]])
    print(m.mul_vec(u))  # Expected: [2, -1] (2*1 + (-1)*0, 2*0 + (-1)*1)

    print("\nTest 4: Edge Case - Vectors with Different Dimensions for Dot Product")
    try:
        u = Vector([[1, 2, 3]])
        v = Vector([[4, 5]])
        print(u.mul_vec(v))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 5: Edge Case - Multiplication with Unsupported Type (string)")
    try:
        v = Vector([[1, 2, 3]])
        print(v * "invalid")  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 6: Edge Case - Incompatible Matrix-Vector Multiplication")
    try:
        u = Vector([[1, 2, 3]])
        m = Matrix([[1, 2], [3, 4]])
        print(m.mul_vec(u))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)


    print("\nTest 7: Matrix-Scalar Multiplication")
    m = Matrix([[1, 2], [3, 4]])
    print(m * 2)  # Expected: [[2, 4], [6, 8]]

    m = Matrix([[0, -1], [-2, 3]])
    print(m * (-3))  # Expected: [[0, 3], [6, -9]]

    print("\nTest 8: Edge Case - Empty Vector")
    try:
        v = Vector([])
        print(v.mul_vec(2))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)


    print("\nTest 9: Edge Case - Empty Matrix")
    try:
        m = Matrix([[]])
        v = Vector([[1, 2, 3]])
        print(m.mul_vec(v))  # Expected: Error
    except ValueError as e:
        print("Caught an error as expected:", e)

    print("\nTest 10: Dot Product of Vector with Itself")
    u = Vector([[1, 2, 3]])
    print(u.mul_vec(u))  # Expected: 14 (1*1 + 2*2 + 3*3)

    print("\nTest 11: Column Vector and Compatible Matrix Multiplication")
    u = Vector([[1], [2], [3]])
    m = Matrix([[4, 5, 6]])
    print(m.mul_vec(u))  # Expected: [32] (4*1 + 5*2 + 6*3)

    print("\nTest 12: Dot Product of Perpendicular Vectors")
    u = Vector([[1, 0]])
    v = Vector([[0, 1]])
    print(u.mul_vec(v))  # Expected: 0 (since they are perpendicular)

if __name__ == "__main__":
    main()
