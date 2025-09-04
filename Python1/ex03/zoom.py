import numpy as np


def zoom_image(image_array: np.ndarray, size=(400, 400)) -> np.ndarray:
    """
    Zoom sur une région centrale de l'image et convertit en niveau de gris.

    Args:
        image_array (np.ndarray): Image RGB sous forme de tableau NumPy.
        size (tuple): Dimensions (hauteur, largeur) du zoom.

    Excepts:
        Vérifie que le zoom est plus petit que l'image d'origine
        Vérifie que l'image en RGB avant de la convertir en B&W
    Returns:
        np.ndarray: Image zoomée en niveaux de gris avec une seule couche.
    """
    try:
        h, w = image_array.shape[:2]
        zoom_h, zoom_w = size

        if zoom_h > h or zoom_w > w:
            raise ValueError("Zoom size exceeds image dimensions.")

        x_center, y_center = w // 2, h // 2
        x_start = x_center - zoom_w // 2
        y_start = y_center - zoom_h // 2

        zoomed = image_array[y_start:y_start + zoom_h,
                             x_start:x_start + zoom_w]

        # Conversion en niveaux de gris (luminosité moyenne)
        if zoomed.ndim == 3 and zoomed.shape[2] == 3:
            zoomed_gray = np.dot(zoomed[..., :3], [0.2989, 0.5870, 0.1140])
            zoomed_gray = zoomed_gray.astype(np.uint8)
            zoomed_gray = zoomed_gray[:, :, np.newaxis]
        else:
            zoomed_gray = zoomed

        return zoomed_gray

    except Exception as error:
        print(f"Erreur lors du zoom : {error}")
        return None
