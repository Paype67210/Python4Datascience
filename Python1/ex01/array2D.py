from typing import Union

Number = Union[int, float]


def slice_me(family: list, start: int, end: int) -> list:
    """
    Function du slice the family list as a list from start to end
    Args: family is a list of INT or FLOAT or a list of INT/FLOAT's lists
        start & end are both INT
    Exceptions:  If entries are not in the right format
    Return: a list sliced
    """
    if not isinstance(family, list) or not all(isinstance(row, list)
                                               for row in family):
        raise TypeError("The entry must be a 2D-list")
    if len(set(len(row) for row in family)) != 1:
        raise TypeError("All raws must have the same lenght.")
    if not all(isinstance(element, (int | float)) for row in family
               for element in row):
        raise ValueError("All the entries must be INT or FLOAT.")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start & End must be INT.")

    return family[start:end]
