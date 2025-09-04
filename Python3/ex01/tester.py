# Tester

from S1E7 import Lannister, Baratheon

# Test Baratheon instance
Arthur = Baratheon("Arthur")
print(Arthur.__dict__)
print(Arthur.__str__)
print(Arthur.__repr__)
print(Arthur.is_alive)
Arthur.die()
print(Arthur.is_alive)
print(Arthur.__doc__)
print("---")

# Test create_baratheon class method
Phoebus = Baratheon.create_baratheon("Phoebus", True)
print(f"Name : {Phoebus.first_name, type(Phoebus).__name__}, Alive : {Phoebus.is_alive}")
print("---")

# Test Lannister instance
Myra = Lannister("Myra")
print(Myra.__dict__)
print(Myra.__str__)
print(Myra.__repr__)
print(Myra.is_alive)
Myra.die()
print(Myra.is_alive)
print(Myra.__doc__)
print("---")

# Test create_lannister class method
Sylvie = Lannister.create_lannister("Sylvie", True)
print(f"Name : {Sylvie.first_name, type(Sylvie).__name__}, Alive : {Sylvie.is_alive}")
print("---")
