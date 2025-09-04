# class Calculs:
#     @staticmethod
def square(x: int | float) -> int | float:
    """ Compute and return the square of the input."""
    if not isinstance(x, (int, float)):
        raise ValueError("Arg must be an INT or a FLOAT!")
    return x * x

    # @staticmethod
def pow(x: int | float) -> int | float:
    """Compute x raised to the power of x (x^x)."""
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be an int or a float.")
    return x ** x

def outer(x: int | float, function) -> object:
    """ Compute and return the result of the requested function applied to the input."""
    if not isinstance(x, (int, float)):
        raise ValueError("1st Arg must be an INT or a FLOAT!")
    if function not in [pow, square]:
        raise ValueError("2nd Arg must be a function (square or pow)!")

    count = 0 # ne sert à rien dans cet exercice
    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)  # Appliquer la fonction au résultat précédent
        return x

    return inner
