from S1E9 import Character

class Baratheon(Character):
    """Concrete class representing a Baratheon character."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        self.is_alive = False

    @classmethod
    def create_baratheon(cls, first_name: str, is_alive: bool = True):
        return cls(first_name, is_alive)

class Lannister(Character):
    """Concrete class representing a Lannister character."""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def die(self) -> None:
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        return cls(first_name, is_alive)

def create_baratheon(func):
    """Decorator to create Baratheon characters from a function returning names."""
    def wrapper(*args, **kwargs):
        names = func(*args, **kwargs)
        return Baratheon.create(*names)
    return wrapper
