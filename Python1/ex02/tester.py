from load_image import ft_load


def test_ft_load():
    try:
        # Test with a valid image path
        img = ft_load("./landscape.jpg")
        print("Array de pixels RGB (premiers 3x3 pixels):")
        print(img[:3, :3])
        print(
            f"Exemple du premier pixel: {img[0, 0]} = "
            f"[R={img[0, 0, 0]}, G={img[0, 0, 1]}, B={img[0, 0, 2]}]"
        )
    except Exception as error:
        print(f"Erreur lors du chargement de l'image: {error}")


if __name__ == "__main__":
    test_ft_load()
    # Tests with an invalid path or a non-image file
    try:
        ft_load("./invalid_path.jpg")
    except Exception as error:
        print(f"Erreur attendue pour un chemin invalide: {error}")

    try:
        ft_load("./not_an_image.txt")
    except Exception as error:
        print(f"Erreur attendue pour un fichier non image: {error}")
