from mathh import Matrix, Vector

def linear_combination(u, coefs):
    if u:
        shaping = u[0].shape
        if any(shaping != vecteur.shape for vecteur in u ):
            raise ValueError("All vector must have the same shape")
        len_vecteur = shaping[1] if shaping[0] == 1 else shaping[0]
        if (len(u) != len(coefs) ):
            raise ValueError("we must have the same number of coefficients as vectors")
        result = Vector([[0.0 for _ in range(shaping[1])] for _ in range(shaping[0])])

        len_1 = 0
        for i in range(shaping[0]):
            for j in range(shaping[1]):
                for z in range(len(u)):
                    result.data[i][j] += u[z].data[i][j] * coefs[z]
                len_1 += 1
        return result	
    else:
        raise ValueError("There is no vector")
        


def main():
    # Basic tests
    e1 = Vector([[1., 0., 0.]])
    e2 = Vector([[0., 1., 0.]])
    e3 = Vector([[0., 0., 1.]])
    
    print("Basic Test 1:")
    result = linear_combination([e1, e2, e3], [10., -2., 0.5])
    print("Expected: [10.0, -2.0, 0.5]")
    print("Result  :", result)
    print()

    v1 = Vector([[1., 2., 3.]])
    v2 = Vector([[0., 10., -100.]])
    
    print("Basic Test 2:")
    result = linear_combination([v1, v2], [10., -2.])
    print("Expected: [10.0, 0.0, 230.0]")
    print("Result  :", result)
    print()
    
    # Edge cases
    print("Edge Case 1: Empty lists")
    try:
        result = linear_combination([], [])
        print("Expected: []")
        print("Result  :", result)
    except ValueError as e:
        print("Caught an error:", e)
    print()

    print("Edge Case 2: Mismatched lengths")
    try:
        result = linear_combination([v1, v2], [10.])
        print("Test failed: Mismatched lengths were accepted.")
    except ValueError as e:
        print("Caught an error for mismatched lengths:", e)
    print()

    print("Edge Case 3: Vectors of different sizes")
    try:
        v3 = Vector([[1., 2.]])
        result = linear_combination([v1, v3], [10., -2.])
        print("Test failed: Vectors of different sizes were accepted.")
    except ValueError as e:
        print("Caught an error for vectors of different sizes:", e)
    print()

    print("Edge Case 4: Zero coefficients")
    result = linear_combination([v1, v2], [0., 0.])
    print("Expected: [0.0, 0.0, 0.0]")
    print("Result  :", result)
    print()

if __name__ == "__main__":
    main()
