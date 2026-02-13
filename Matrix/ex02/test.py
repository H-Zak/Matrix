from mathh import Matrix, Vector, lerp



def main():
    print("=== Tests d'interpolation linéaire (lerp) ===")

    print("Tests avec des nombres :")
    print("lerp(0., 1., 0.) =", lerp(0., 1., 0.))  # Attendu: 0.0
    print("lerp(0., 1., 1.) =", lerp(0., 1., 1.))  # Attendu: 1.0
    print("lerp(0., 1., 0.5) =", lerp(0., 1., 0.5))  # Attendu: 0.5
    print("lerp(21., 42., 0.3) =", lerp(21., 42., 0.3))  # Attendu: 27.3

    print("\nTests avec des Vecteurs :")
    v1 = Vector([[2., 1.]])
    v2 = Vector([[4., 2.]])
    print("Vecteurs :", v1, "et", v2)
    print("lerp avec t=0.3 :", lerp(v1, v2, 0.3))  # Attendu: [2.6, 1.3]

    v3 = Vector([[0., 0.]])
    v4 = Vector([[10., 10.]])
    print("lerp avec t=0.5 :", lerp(v3, v4, 0.5))  # Attendu: [5.0, 5.0]

    print("\nTests avec des Matrices :")
    m1 = Matrix([[2., 1.], [3., 4.]])
    m2 = Matrix([[20., 10.], [30., 40.]])
    print("Matrices :")
    print("M1 :", m1)
    print("M2 :", m2)
    print("lerp avec t=0.5 :", lerp(m1, m2, 0.5))  # Attendu: [[11.0, 5.5], [16.5, 22.0]]

    m3 = Matrix([[0., 0.], [0., 0.]])
    m4 = Matrix([[1., 2.], [3., 4.]])
    print("lerp avec t=1.0 :", lerp(m3, m4, 1.0))  # Attendu: [[1.0, 2.0], [3.0, 4.0]]

    print("\n=== Tests des cas limites ===")

    print("Cas limite : t hors de [0, 1]")
    try:
        lerp(0., 1., 1.5)
    except ValueError as e:
        print("Erreur capturée :", e)

    print("Cas limite : Vecteurs de tailles différentes")
    try:
        v5 = Vector([[1., 2.]])
        v6 = Vector([[1., 2., 3.]])
        lerp(v5, v6, 0.5)
    except ValueError as e:
        print("Erreur capturée :", e)

    print("Cas limite : Matrices de tailles différentes")
    try:
        m5 = Matrix([[1., 2.], [3., 4.]])
        m6 = Matrix([[1., 2., 3.], [4., 5., 6.]])
        lerp(m5, m6, 0.5)
    except ValueError as e:
        print("Erreur capturée :", e)

if __name__ == "__main__":
    main()
