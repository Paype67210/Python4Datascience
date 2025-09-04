from abc import ABC, abstractmethod

class Character(ABC):
  """
  Abstract class Character: No Instance is possible!

  Args:
    first_name (str): the name of the character
    is_alive (bool): defined as True by definition. Is an optional parameter
  """

  def __init__(self, first_name: str, is_alive: bool = True) -> None:
    if not isinstance(first_name, str):
      raise TypeError("First_name must be a string.")
    if not isinstance(is_alive, bool):
      raise TypeError("Is_alive must be a boolean.")
    self.first_name = first_name
    self.is_alive = is_alive
  
  @abstractmethod
  def die(self) -> None:
    """
    Change the status of the character as Died.
    Would be instanciated inside the inheritated class!
    """
    pass

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Stark(Character):
  """
  Concrete class represeting a Starck Character

  Args : not defined here cause of inheritated parameters
  """
  def die(self) -> None:
    """ Define the status of the Stark as Died"""
    self.is_alive = False
