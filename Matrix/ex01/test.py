from mathh import Matrix, Vector, linear_combination


def main():
    print("=== Tests de la combinaison linéaire ===")

    e1 = Vector([[1., 0., 0.]])
    e2 = Vector([[0., 1., 0.]])
    e3 = Vector([[0., 0., 1.]])

    print("Test de base 1 : Vecteurs de base")
    print("Vecteurs :", e1, e2, e3)
    print("Coefficients : [10., -2., 0.5]")
    result = linear_combination([e1, e2, e3], [10., -2., 0.5])
    print("Résultat attendu : [10.0, -2.0, 0.5]")
    print("Résultat obtenu :", result)
    print()

    v1 = Vector([[1., 2., 3.]])
    v2 = Vector([[0., 10., -100.]])

    print("Test de base 2 : Vecteurs génériques")
    print("Vecteurs :", v1, v2)
    print("Coefficients : [10., -2.]")
    result = linear_combination([v1, v2], [10., -2.])
    print("Résultat attendu : [10.0, 0.0, 230.0]")
    print("Résultat obtenu :", result)
    print()

    print("=== Tests des cas limites ===")

    print("Cas limite 1 : Listes vides")
    try:
        result = linear_combination([], [])
        print("Résultat :", result)
    except ValueError as e:
        print("Erreur capturée :", e)
    print()

    print("Cas limite 2 : Nombre de coefficients différent")
    try:
        result = linear_combination([v1, v2], [10.])
        print("Échec : Longueurs différentes acceptées.")
    except ValueError as e:
        print("Succès : Erreur capturée pour longueurs différentes :", e)
    print()

    print("Cas limite 3 : Vecteurs de tailles différentes")
    try:
        v3 = Vector([[1., 2.]])
        result = linear_combination([v1, v3], [10., -2.])
        print("Échec : Tailles différentes acceptées.")
    except ValueError as e:
        print("Succès : Erreur capturée pour tailles différentes :", e)
    print()

    print("Cas limite 4 : Coefficients nuls")
    result = linear_combination([v1, v2], [0., 0.])
    print("Résultat attendu : [0.0, 0.0, 0.0]")
    print("Résultat obtenu :", result)
    print()

if __name__ == "__main__":
    main()
