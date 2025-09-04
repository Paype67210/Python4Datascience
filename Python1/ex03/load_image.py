import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load image from specified path, return it as a NumPy array in RGB format.

    Args:
        path (str): The file path to the image.

    Returns:
        array: loaded img as NumPy array with shape (h, w, 3) for RGB pixels.
    """

    valid_formats = ['JPEG', 'JPG', 'PNG', 'BMP']
    try:
        # Attempt to open the image file
        img = Image.open(path)
        # Verify the real format of the image
        if img.format not in valid_formats:
            raise ValueError(
                f"Wrong Image Format: {img.format}. Allowed: "
                f"{', '.join(valid_formats)}"
            )
        # Convert to RGB to ensure 3 channels
        img = img.convert('RGB')
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found at path: {path}")
    except IOError:
        raise IOError(f"Could not open image file at path: {path}")

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Print image information
    print(f"The shape of image is: {img_array.shape}")
    print(f"Height: {img_array.shape[0]}, Width: {img_array.shape[1]}")

    return img_array
