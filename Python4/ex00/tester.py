from statistics import ft_statistics
""" Tester pour démontrer le fonctionnement de statistics.py"""

# -----------------------------
# 🔍 TESTS
# -----------------------------

print("Test 1 : Aucun float ou int")
ft_statistics("a", "dfgh", True, tutu="mean")

print("\nTest 2 : Toutes les valeurs sont à 0")
ft_statistics(0.0, 0.0, 0.0, tutu="mean")

print("\nTest 3 : Liste trop courte")
ft_statistics(1.0, tutu="mean", tata="median")

print("\nTest 4 : kwarg invalide")
ft_statistics(1.0, 2.0, 3.0, tutu="moyenne")

print("\nTest 5 : Calculs valides")
ft_statistics(1.0, 2.0, 5.0, 14.0, 75.0, tutu="mean", tata="median", toto="quartile", titi="std", tyty="var") 

print("===== Fin des tests =====")
