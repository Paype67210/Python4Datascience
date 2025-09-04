import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def test_filters(path: str) -> None:
    """Applique les filtres de couleur à une image et affiche les résultats."""
    try:
        array = ft_load(path)
    except Exception as error:
        print(f"[Loading failed] {error}")
        return

    filters = [
        ("Inverted", ft_invert),
        ("Red filter", ft_red),
        ("Green filter", ft_green),
        ("Blue filter", ft_blue),
        ("Grey filter", ft_grey),
    ]

    for name, func in filters:
        try:
            print(f"\n--- {name} ---")
            filtered = func(array)
            print(filtered)
            plt.imshow(filtered)
            plt.title(name)
            plt.xlabel("X axis")
            plt.ylabel("Y axis")
            plt.show()
        except Exception as error:
            print(f"[Erreur {name}] {error}")

    try:
        print("\n--- Docstring de ft_invert ---")
        print(ft_invert.__doc__)
    except Exception as error:
        print(f"[Error docstring] {error}")


if __name__ == "__main__":

    image_array = ft_load("./landscape.jpg")

    print("\n=== Test des filtres sur landscape.jpg ===")
    try:
        plt.imshow(image_array)
        plt.title("Image originale")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    except Exception as error:
        print(f"[Erreur affichage image originale] {error}")

    test_filters("./landscape.jpg")
