import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received using only =, +, -, *
    """
    try:
        inverted = array * 0 + 255 - array
        return inverted
    except Exception as error:
        print(f"Error inverting image : {error}")
        return None


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel of the image using only =, *
    """
    try:
        red = array * 1
        red[:, :, 1] = red[:, :, 1] * 0
        red[:, :, 2] = red[:, :, 2] * 0
        return red
    except Exception as error:
        print(f"Error reding image : {error}")
        return None


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel of the image using only =, -
    """
    try:
        green = array - array
        green[:, :, 1] = array[:, :, 1]
        return green
    except Exception as error:
        print(f"Error greening image : {error}")
        return None


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel of the image using only =
    """
    try:
        blue = array.copy()
        blue[:, :, 0] = 0
        blue[:, :, 1] = 0
        return blue
    except Exception as error:
        print(f"Error bluing image : {error}")
        return None


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale using average method using only =, /
    """
    try:
        grey = (
            array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3
        ).astype(np.uint8)
        grey = grey[:, :, np.newaxis]
        grey = np.repeat(grey, 3, axis=2)
        return grey
    except Exception as error:
        print(f"Error greying image : {error}")
        return None
