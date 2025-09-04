class Calculator:
    """A calculator class for vector operations."""

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        """Compute and print the dot product of two vectors."""
        result = sum(x * y for x, y in zip(v1, v2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        """Compute and print the element-wise addition of two vectors."""
        result = [x + y for x, y in zip(v1, v2)]
        print(f"Addition Vector is : {result}")

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        """Compute and print the element-wise subtraction of two vectors."""
        result = [x - y for x, y in zip(v1, v2)]
        print(f"Soustract Vector is: {result}")
