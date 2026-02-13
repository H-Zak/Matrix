from mathh import Matrix, Vector

def main():
    print("=== Tests du produit scalaire (dot product) ===")

    print("Tests de base avec des vecteurs :")
    u = Vector([[0., 0.]])
    v = Vector([[1., 1.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 0.0

    u = Vector([[1., 1.]])
    v = Vector([[1., 1.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 2.0

    u = Vector([[-1., 6.]])
    v = Vector([[3., 2.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 9.0

    print("\nTests avec des vecteurs de plus grande dimension :")
    u = Vector([[1., 2., 3.]])
    v = Vector([[4., 5., 6.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 32.0 (1*4 + 2*5 + 3*6)

    u = Vector([[0., 1., 0.]])
    v = Vector([[0., 1., 0.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 1.0

    print("\nTests avec des vecteurs orthogonaux :")
    u = Vector([[1., 0., 0.]])
    v = Vector([[0., 1., 0.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 0.0

    print("\n=== Tests des cas limites ===")

    print("Cas limite : Vecteurs de tailles différentes")
    try:
        u = Vector([[1., 2.]])
        v = Vector([[1., 2., 3.]])
        print(u.dot(v))
    except ValueError as e:
        print("Erreur capturée :", e)

    print("Cas limite : Vecteurs avec des zéros")
    u = Vector([[0., 0., 0.]])
    v = Vector([[0., 0., 0.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 0.0

    u = Vector([[0., 0., 1.]])
    v = Vector([[0., 1., 0.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 0.0

    print("Cas limite : Vecteurs avec des valeurs négatives")
    u = Vector([[-1., -2., -3.]])
    v = Vector([[-4., -5., -6.]])
    print("u.dot(v) =", u.dot(v))  # Attendu: 32.0

    print("Test avec des vecteurs colonnes")
    u_col = Vector([[1.], [2.]])  # Column vector
    v_col = Vector([[3.], [4.]])  # Column vector
    print("u_col.dot(v_col) =", u_col.dot(v_col))  # Attendu: 1*3 + 2*4 = 11.0

if __name__ == "__main__":
    main()
