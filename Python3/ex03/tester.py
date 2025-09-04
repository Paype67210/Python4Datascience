from ft_calculator import Calculator

v1 = Calculator([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
print(f"Création du vecteur de travail: {v1.vector}")
print("Test 1 : Addition d’un scalaire à un vecteur")
v1 + 5
print("---")

print("Test 2 : Multiplication d’un vecteur par un scalaire")
v1 * 5
print("---")

print("Test 3 : Soustraction d’un scalaire à un vecteur")
v1 - 5
print("---")

print("Test 4 : Division d’un vecteur par un scalaire")
v1 / 5
print("---")

print("Test 5 : Division par zéro (gestion d’erreur)")
v1 / 0
print("---")
