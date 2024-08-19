from mathh import Matrix, Vector

# que se passe t il si vector est vide 
def main():
    # Test de base avec des vecteurs nuls
    print("Basic tests with zero vectors:")
    
    u = Vector([[0., 0., 0.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 0.0, 0.0, 0.0

    # Test de base avec un vecteur simple
    print("\nBasic tests with simple vectors:")
    
    u = Vector([[1., 2., 3.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 6.0, 3.74165738, 3.0
    
    u = Vector([[-1., -2.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 3.0, 2.236067977, 2.0
    
    # Cas limite : Vecteur avec des valeurs négatives
    print("\nEdge cases with negative values:")
    
    u = Vector([[-3., -4., -5.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 12.0, 7.07106781187, 5.0
    
    u = Vector([[-1., -1., -1., -1.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 4.0, 2.0, 1.0
    
    # Cas limite : Vecteur avec des valeurs positives et négatives mélangées
    print("\nEdge cases with mixed values:")
    
    u = Vector([[1., -1., 1., -1.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 4.0, 2.0, 1.0
    
    u = Vector([[3., -2., 1.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 6.0, 3.74165738677, 3.0
    
    # Cas limite : Vecteur avec des grands nombres
    print("\nEdge cases with large numbers:")
    
    u = Vector([[1000., 2000., 3000.]])
    print(u.norm_1(), u.norm(), u.norm_inf())  # Expected: 6000.0, 3741.65738677, 3000.0

if __name__ == "__main__":
    main()