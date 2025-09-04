import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from zoom import zoom_image


def test_image(path: str, zoom_size=(300, 300)) -> None:
    """
    Charge image, affiche originale, applique zoom et affiche le résultat.

    Args:
      path est le chemin de l'image d'origine
      zoom_size est le zoom souhaité en pixels

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
        zoomed = zoom_image(image_array, size=zoom_size)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
    except Exception as error:
        print(f"[Erreur zoom] {error}")
        return

    try:
        plt.imshow(np.squeeze(zoomed), cmap="gray")
        plt.title("Image zoomée en niveaux de gris")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    except Exception as error:
        print(f"[Erreur affichage image zoomée] {error}")


if __name__ == "__main__":
    print("\n--- Test 1 : Image valide ---")
    try:
        test_image("./animal.jpeg", zoom_size=(300, 300))
    except Exception as error:
        print(f"Erreur capturée : {error}")

    print("\n--- Test 2 : Zoom trop grand ---")
    try:
        test_image("./animal.jpeg", zoom_size=(2000, 2000))
    except Exception as error:
        print(f"Erreur capturée : {error}")

    print("\n--- Test 3 : Fichier inexistant ---")
    try:
        test_image("not_found.jpeg", zoom_size=(300, 300))
    except Exception as error:
        print(f"Erreur capturée : {error}")

    print("\n--- Test 4 : Format non supporté ---")
    try:
        test_image("./not_an_image.txt", zoom_size=(300, 300))
    except Exception as error:
        print(f"Erreur capturée : {error}")
