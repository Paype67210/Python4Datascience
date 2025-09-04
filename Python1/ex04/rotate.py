import numpy as np


def rotate_image(image_array: np.ndarray) -> np.ndarray:
    """
    Effectue transpo (rotation de 90° dans le sens horaire) d'image initiale

    Args:
        image_array (np.ndarray): Image RGB sous forme de tableau NumPy.

    Returns:
        np.ndarray: Image pivotée.
    """
    try:
        height, width = image_array.shape[:2]
        channels = image_array.shape[2] if image_array.ndim == 3 else 1

        # Initialiser un tableau vide pour l'image pivotée
        rotated = np.zeros((width, height, channels), dtype=image_array.dtype)

        # Remplir manuellement le tableau pivoté
        for i in range(height):
            for j in range(width):
                if channels == 1:  # Cas d'une image avec un seul canal
                    rotated[j, height - 1 - i] = image_array[i, j]
                else:  # Cas d'une image RGB
                    rotated[j, height - 1 - i, :] = image_array[i, j, :]

        return rotated

    except Exception as error:
        print(f"Erreur lors de la transposition : {error}")
        return image_array
