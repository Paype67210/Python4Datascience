from typing import Union
import numpy as np

Number = Union[int, float]


def give_bmi(height: list[Number], weight: list[Number]) -> list[float]:
    """
    Function to calculate the bmi
    Args:  height is a list of int or float
           weight is a list of int or float
    Exceptions:   height & weight must be int or float
                  both lists must have the same length
                  height cannot be null (impossible calculation)
    return: list of bmi calculated in float
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height & weight must be lists.")

    if len(height) != len(weight):
        raise ValueError("Both lists must have the same lenght.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All elements in height must be int or float.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All elements in weight must be int or float.")

    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)

    if np.any(height_array == 0):
        raise ValueError("Height value cannot be null.")

    bmi_array = weight_array / (2 ** height_array)
    return bmi_array.tolist()


def apply_limit(bmi: list[Number], limit: int) -> list[bool]:
    """
    Function to know if the bmi is higher than the limit definined
    Args:  bmi is a ist of bmi calculation in float or int
           limit is the defined hight level in INT
    Exceptions:  The different values must be float or int
    Return: list of true/false value depending of the result of give_bmi
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")
    if not all(isinstance(b, float) for b in bmi):
        raise TypeError("All elements in BMI must be a FLOAT.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an INT.")
    return [b > limit for b in bmi]
