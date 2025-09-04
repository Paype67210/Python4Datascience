from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """ Creation of a New Stark Character as a King of both families"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        # King inherits from Baratheon and Lannister.
        # According to Python's Method Resolution Order (MRO), Baratheon is prioritized.
        # Therefore, attributes like 'eyes' and 'hairs' will initially come from Baratheon:
        # eyes = 'brown', hairs = 'dark'
        # These can be modified later using set_eyes() and set_hairs().
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str) -> None:
        """
        set_eyes allows dynamic modification of the 'eyes' attribute
        regardless of the inherited default value.
        """
        self.eyes = color

    def get_eyes(self) -> str:
        return self.eyes

    def set_hairs(self, color: str) -> None:
        """
        set_hairs allows dynamic modification of the 'hairs' attribute
        regardless of the inherited default value.
        """
        self.hairs = color

    def get_hairs(self) -> str:
        return self.hairs
