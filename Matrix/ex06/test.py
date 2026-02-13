from mathh import Matrix, Vector, cross_product
def main():
    print("Basic tests with unit vectors:")

    u = Vector([[0., 0., 1.]])
    v = Vector([[1., 0., 0.]])
    print(cross_product(u,v))  # Expected: [0., 1., 0.]

    print("\nTests with non-unit vectors:")

    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(cross_product(u,v))  # Expected: [-3., 6., -3.]

    u = Vector([[4., 2., -3.]])
    v = Vector([[-2., -5., 16.]])
    print(cross_product(u,v))  # Expected: [17., -58., -16.]

    print("\nEdge case: Cross product of a vector with itself")

    u = Vector([[1., 2., 3.]])
    print(cross_product(u, u))  # Expected: [0., 0., 0.]

    print("\nEdge case: Vectors of different sizes")
    try:
        u = Vector([[1., 2., 3.]])
        v = Vector([[1., 2.]])
        print(cross_product(u,v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)

    print("\nEdge case: Vectors with zero components")

    u = Vector([[1., 0., 0.]])
    v = Vector([[0., 1., 0.]])
    print(cross_product(u,v))  # Expected: [0., 0., 1.]

    u = Vector([[0., 1., 0.]])
    v = Vector([[0., 0., 1.]])
    print(cross_product(u,v))  # Expected: [1., 0., 0.]

    print("\nTests with mixed vector shapes (row and column):")
    u_row = Vector([[1., 0., 0.]])  # Row vector
    v_col = Vector([[0.], [1.], [0.]])  # Column vector
    print(cross_product(u_row, v_col))  # Expected: [0., 0., 1.]

if __name__ == "__main__":
    main()
