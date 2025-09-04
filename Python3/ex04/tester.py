from ft_calculator import Calculator

a = [5.0, 10.0, 2.0]
b = [2.0, 4.0, 3.0]

print("Vecteur A :", a)
print("Vecteur B :", b)

print("\n--- Produit scalaire ---")
Calculator.dotproduct(a, b)

print("\n--- Addition des vecteurs ---")
Calculator.add_vec(a, b)

print("\n--- Soustraction des vecteurs ---")
Calculator.sous_vec(a, b)
