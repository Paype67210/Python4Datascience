import unittest
from E1S9 import Stark, Character

class TestCharacter(unittest.TestCase):
    """
    Classe de tests Unitaires de S1E9
    """
    def test_stark_initialization(self):
        """ Test de création d'un personnage sans définir son status alive / dead"""  
        stark = Stark("Myra")
        self.assertEqual(
            stark.first_name, "Myra",
            msg="❌ Le prénom du personnage Stark devrait être 'Myra'."
        )
        self.assertTrue(
            stark.is_alive,
            msg="❌ Le personnage Stark devrait être vivant par défaut."
        )

    def test_stark_die_method(self):
        """ Test de création d'un personnage puis utilisation de la méthode die()"""  
        stark = Stark("Phoebus")
        stark.die()
        self.assertFalse(
            stark.is_alive,
            msg="❌ Après appel à die(), le personnage Stark devrait être mort."
        )

    def test_stark_is_alive_custom(self):
        """ Test de création d'un personnage déjà mort à la création"""  
        stark = Stark("Phoebus", is_alive=False)
        self.assertFalse(
            stark.is_alive,
            msg="❌ Le paramètre is_alive devrait pouvoir être défini à False à l'initialisation."
        )

    def test_invalid_first_name_type(self):
        """ Test avec un nom qui n'est pas un str"""
        with self.assertRaises(TypeError, msg="❌ Le prénom doit être une chaîne de caractères."):
            Stark(123)

    def test_invalid_is_alive_type(self):
        """ Test avec is_alive qui n'est pas un booléen"""
        with self.assertRaises(TypeError, msg="❌ is_alive doit être un booléen."):
            Stark("André", is_alive="yes")

    def test_invalid_creation_of_a_character(self):
        """ Test d'instanciation de la classe abstraite"""
        with self.assertRaises(TypeError, msg="❌ La classe abstraite Character ne devrait pas pouvoir être instanciée."):
            Character("Popaul")

if __name__ == "__main__":
    """ Fonction de test de la classe Stark"""  
    print("\n=== DÉMARRAGE DES TESTS UNITAIRES POUR LA CLASSE STARK ===\n")
    unittest.main(verbosity=2)

