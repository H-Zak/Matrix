from mathh import Matrix, Vector


def main():
    print("=== Tests des opérations sur les Vecteurs ===")
    u = Vector([[2., 3.]])
    v = Vector([[5., 7.]])

    print("Vecteur u :", u)
    print("Vecteur v :", v)
    u.add(v)
    print("Résultat de u + v :", u)

    u = Vector([[2., 3.]])
    u.sub(v)
    print("Résultat de u - v :", u)

    u = Vector([[2., 3.]])
    u.scl(2)
    print("Résultat de u * 2 :", u)

    print("\n=== Tests des opérations sur les Matrices ===")
    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    v = Matrix([
        [7., 4.],
        [-2., 2.]
    ])

    print("Matrice u :")
    print(u)
    print("Matrice v :")
    print(v)
    u.add(v)
    print("Résultat de u + v :")
    print(u)

    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    u.sub(v)
    print("Résultat de u - v :")
    print(u)  # Attendu: [-6.0, -2.0] [5.0, 2.0]

    u = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    u.scl(2)
    print("Résultat de 2 * u :")
    print(u)  # Attendu: [2.0, 4.0] [6.0, 8.0]

    print("\n=== Tests des cas limites ===")
    print("Test 1: Vecteurs de tailles différentes")
    try:
        u = Vector([[1., 2., 3.]])
        v = Vector([[4., 5.]])
        u.add(v)
    except ValueError as e:
        print("Erreur capturée (tailles différentes) :", e)

    print("Test 2: Matrices de tailles différentes")
    try:
        u = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        v = Matrix([
            [1., 2., 3.],
            [4., 5., 6.]
        ])
        u.add(v)
    except ValueError as e:
        print("Erreur capturée (tailles différentes) :", e)

    print("Test 3: Matrice avec lignes de longueurs différentes")
    try:
        u = Matrix([
            [1., 2.],
            [3., 4., 5.]  # Ligne avec 3 éléments au lieu de 2
        ])
        print("Échec : Matrice acceptée malgré lignes inégales.")
    except ValueError as e:
        print("Succès : Erreur capturée pour lignes inégales :", e)

    print("Test 4: Matrice vide")
    try:
        u = Matrix([])  # Matrice vide
        print("Succès : Matrice vide acceptée.")
    except ValueError as e:
        print("Échec : Erreur capturée pour matrice vide :", e)

    print("Test 5: Matrice avec une ligne vide")
    try:
        u = Matrix([
            [1., 2.],
            []  # Ligne vide
        ])
        print("Échec : Matrice acceptée malgré ligne vide.")
    except ValueError as e:
        print("Succès : Erreur capturée pour ligne vide :", e)

    print("Test 6: Matrice avec éléments non numériques")
    try:
        u = Matrix([
            [1., 2.],
            [3., "a"]  # Élément non numérique
        ])
        print("Échec : Matrice acceptée malgré éléments invalides.")
    except ValueError as e:
        print("Succès : Erreur capturée pour éléments non numériques :", e)

    print("Test 7: Méthode add() avec matrices de tailles différentes")
    try:
        u = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        v = Matrix([
            [1., 2., 3.],
            [4., 5., 6.]
        ])
        u.add(v)  # Tailles incompatibles
        print("Échec : Addition acceptée malgré tailles différentes.")
    except ValueError as e:
        print("Succès : Erreur capturée pour add() :", e)

    print("Test 8: Méthode sub() avec matrices de tailles différentes")
    try:
        u = Matrix([
            [1., 2.],
            [3., 4.]
        ])
        v = Matrix([
            [1., 2.],  # Taille incompatible
        ])
        u.sub(v)
        print("Échec : Soustraction acceptée malgré tailles différentes.")
    except ValueError as e:
        print("Succès : Erreur capturée pour sub() :", e)

    print("Test 9: Matrice avec objets complexes")
    try:
        u = Matrix([
            [1., 2.],
            [{"key": "value"}, 3.]  # Élément complexe
        ])
        print("Échec : Matrice acceptée malgré objets invalides.")
    except ValueError as e:
        print("Succès : Erreur capturée pour objets complexes :", e)





if __name__ == "__main__":
    main()
