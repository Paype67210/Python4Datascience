# Tester.py

from DiamondTrap import King

# Test King Joffrey instance
Jeoffrey = King("Jeoffrey")
print(Jeoffrey.__dict__)
Jeoffrey.set_eyes("blue")
Jeoffrey.set_hairs("light")
print(Jeoffrey.get_eyes())
print(Jeoffrey.get_hairs())
print(Jeoffrey.__dict__)
print("---")
