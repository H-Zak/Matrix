from mathh import Matrix, Vector

def main():
    # Test 1: Transposition d'une matrice 2x3
    print("Test 1: Transpose of a 2x3 matrix")
    u = Matrix([[1, 2, 3], [4, 5, 6]])
    print("Original:\n", u)
    print("Transposed:\n", u.transpose())  
    # Expected:
    # 1 2 3      1 4
    # 4 5 6      2 5
    #            3 6

    # Test 2: Transposition d'une matrice carrée 3x3
    print("\nTest 2: Transpose of a 3x3 square matrix")
    u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print("Original:\n", u)
    print("Transposed:\n", u.transpose())  
    # Expected:
    # 1 0 0      1 0 0
    # 0 1 0      0 1 0
    # 0 0 1      0 0 1

    # Test 3: Transposition d'une matrice colonne (4x1)
    print("\nTest 3: Transpose of a 4x1 column matrix")
    u = Matrix([[1], [2], [3], [4]])
    print("Original:\n", u)
    print("Transposed:\n", u.transpose())  
    # Expected:
    # 1      1 2 3 4
    # 2
    # 3
    # 4

    # Test 4: Transposition d'une matrice ligne (1x4)
    print("\nTest 4: Transpose of a 1x4 row matrix")
    u = Matrix([[1, 2, 3, 4]])
    print("Original:\n", u)
    print("Transposed:\n", u.transpose())  
    # Expected:
    # 1 2 3 4
    # Transposed:
    # 1
    # 2
    # 3
    # 4

    # Test 5: Cas limite - Matrice vide
    print("\nTest 5: Edge Case - Empty matrix")
    u = Matrix([])
    print("Original:\n", u)
    print("Transposed:\n", u.transpose())  
    # Expected: Empty matrix should return an empty matrix
    
    # Test 6: Transposition d'une grande matrice 4x4
    print("\nTest 6: Transpose of a 4x4 matrix")
    u = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    print("Original:\n", u)
    print("Transposed:\n", u.transpose())  
    # Expected:
    # 1  2  3  4      1  5  9  13
    # 5  6  7  8      2  6  10 14
    # 9  10 11 12     3  7  11 15
    # 13 14 15 16     4  8  12 16

if __name__ == "__main__":
    main()