import matplotlib.pyplot as plt
from load_image import ft_load
from rotate import rotate_image


def test_image(path: str) -> None:
    """
    Charge img, affiche originale, applique transpo et affiche résultat.

    Args:
      path est le chemin de l'image d'origine

    Excepts & Return:
      N/A
    """

    try:
        image_array = ft_load(path)
    except Exception as error:
        print(f"[Erreur chargement] {error}")
        return

    try:
        plt.imshow(image_array)
        plt.title("Image originale")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    except Exception as error:
        print(f"[Erreur affichage image originale] {error}")

    try:
        rotated = rotate_image(image_array)
        print(f"New shape after slicing: {rotated.shape}")
        print(rotated)
    except Exception as error:
        print(f"[Erreur rotation] {error}")
        return

    try:
        plt.imshow(rotated)
        plt.title("Image transposée")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    except Exception as error:
        print(f"[Erreur affichage image transposée] {error}")


if __name__ == "__main__":
    print("\n--- Test 1 : Image valide ---")
    try:
        test_image("./animal.jpeg")
    except Exception as error:
        print(f"Erreur capturée : {error}")

    print("\n--- Test 2 : Fichier inexistant ---")
    try:
        test_image("not_found.jpeg")
    except Exception as error:
        print(f"Erreur capturée : {error}")

    print("\n--- Test 4 : Format non supporté ---")
    try:
        test_image("./not_an_image.txt")
    except Exception as error:
        print(f"Erreur capturée : {error}")
