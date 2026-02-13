from mathh import Matrix, Vector, angle_cos


def main():
    print("Basic tests with identical vectors:")

    u = Vector([[1., 0.]])
    v = Vector([[1., 0.]])
    print(angle_cos(u, v))  # Expected: 1.0

    print("\nBasic tests with orthogonal vectors:")

    u = Vector([[1., 0.]])
    v = Vector([[0., 1.]])
    print(angle_cos(u, v))  # Expected: 0.0

    print("\nBasic tests with opposite vectors:")

    u = Vector([[-1., 1.]])
    v = Vector([[1., -1.]])
    print(angle_cos(u,v))  # Expected: -1.0

    print("\nBasic tests with collinear vectors:")

    u = Vector([[2., 1.]])
    v = Vector([[4., 2.]])
    print(angle_cos(u,v))  # Expected: 1.0

    print("\nTests with higher dimension vectors:")

    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print(angle_cos(u,v))  # Expected: 0.974631846

    print("\nEdge case: Vectors of different sizes")
    try:
        u = Vector([[1., 2.]])
        v = Vector([[1., 2., 3.]])
        print(angle_cos(u ,v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)

    print("\nEdge case: Zero vectors")
    try:
        u = Vector([[0., 0.]])
        v = Vector([[1., 1.]])
        print(angle_cos(u, v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)

    try:
        u = Vector([[0., 0.]])
        v = Vector([[0., 0.]])
        print(angle_cos(u, v))  # Expected: Error
    except ValueError as e:
        print("Caught an error:", e)

if __name__ == "__main__":
    main()
