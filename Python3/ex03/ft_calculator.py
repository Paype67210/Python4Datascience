class Calculator:
    """A calculator class for performing scalar operations on vectors."""

    def __init__(self, vector: list[float]) -> None:
        self.vector = vector

    def __add__(self, scalar: float) -> None:
        result = [x + scalar for x in self.vector]
        print(result)

    def __mul__(self, scalar: float) -> None:
        result = [x * scalar for x in self.vector]
        print(result)

    def __sub__(self, scalar: float) -> None:
        result = [x - scalar for x in self.vector]
        print(result)

    def __truediv__(self, scalar: float) -> None:
        if scalar == 0:
            print("Error: Division by zero.")
            return
        result = [x / scalar for x in self.vector]
        print(result)
