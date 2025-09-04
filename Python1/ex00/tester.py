# test_errors.py

from give_bmi import give_bmi, apply_limit


def test_give_bmi_errors():
    """
    Function for testing the different cases of error for give_bmi
    """
    test_cases = [
        # Mauvais types
        (123, [70]),  # height n'est pas une liste
        ([1.75], "70"),  # weight n'est pas une liste
        ([1.75, "bad"], [70, 80]),  # élément non numérique dans height
        ([1.75, 1.80], [70, "bad"]),  # élément non numérique dans weight
        ([1.75], [70, 80]),  # longueurs différentes
        ([0], [70]),  # division par zéro
    ]

    for i, (h, w) in enumerate(test_cases, 1):
        try:
            give_bmi(h, w)
        except (TypeError, ValueError) as e:
            print(f"Test {i} OK: {e}")
        else:
            print(f"Test {i} ÉCHEC: aucune exception levée")


def test_apply_limit_errors():
    """
    Function for testing the different cases of error for apply_limit
    """
    test_cases = [
        ("not a list", 25),  # bmi n'est pas une liste
        ([22.5, "bad"], 25),  # élément non numérique dans bmi
        ([22.5, 30.1], "high"),  # limit n'est pas un entier
    ]

    for i, (bmi, limit) in enumerate(test_cases, 1):
        try:
            apply_limit(bmi, limit)
        except (TypeError, ValueError) as e:
            print(f"Test {i} OK: {e}")
        else:
            print(f"Test {i} ÉCHEC: aucune exception levée")


if __name__ == "__main__":
    print("Tests de gestion des erreurs pour give_bmi:")
    test_give_bmi_errors()
    print("\nTests de gestion des erreurs pour apply_limit:")
    test_apply_limit_errors()

    print("Tests du bon fonctionnement des deux fonctions:")
    height = [2.71, 1.15, 3.40]
    weight = [165.3, 38.4, 215]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 20))
    except (TypeError, ValueError) as error:
        print(f"Erreur détectée : {error}")
