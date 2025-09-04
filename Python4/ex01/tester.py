from in_out import outer, square, pow

print("===== Test de la fonction square")
my_counter = outer(3, square)
print(my_counter())  # 9
print(my_counter())  # 81
print(my_counter())  # 6561

print("===== Test de la fonction pow")
another_counter = outer(1.5, pow)
print(another_counter())  # 1.8371173070873836
print(another_counter())  # 3.056683336818703
print(another_counter())  # 30.42684786675409

print("===== Test des erreurs")
try:
    outer("not_a_number", square)
except ValueError as error:
    print(f"Erreur attendue (x invalide) : {error}")

try:
    outer(3, "square")  # Mauvais type pour function
except ValueError as error:
    print(f"Erreur attendue (function invalide) : {error}")

try:
    def fake_func(x): return x
    outer(3, fake_func)  # Fonction non autorisée
except ValueError as error:
    print(f"Erreur attendue (fonction non autorisée) : {error}")
