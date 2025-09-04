# Script de test pour Hello.py

import subprocess
import sys

def test_hello():
    # Test la sortie du programme Hello.py
    try:
        # Exécuter Hello.py et capturer la sortie
        result = subprocess.run(['python3', 'Hello.py'], 
                              capture_output=True, text=True, cwd='.')
        
        # Vérifier que le programme s'exécute sans erreur
        if result.returncode != 0:
            print("❌ ERREUR: Le programme a échoué")
            print("Erreur:", result.stderr)
            return False
        
        # Sortie attendue
        expected_lines = [
            "['Hello', 'World!']",
            "('Hello', 'France!')",
            "{'Mulhouse!', 'Hello'}",  # L'ordre dans un set peut varier
            "{'Hello': '42Mulhouse!'}"
        ]
        
        actual_lines = result.stdout.strip().split('\n')
        
        print("=== RÉSULTATS DU TEST ===")
        print("Sortie obtenue:")
        for line in actual_lines:
            print(f"  {line}")
        
        # Vérifier le nombre de lignes
        if len(actual_lines) != len(expected_lines):
            print(f"❌ ERREUR: Nombre de lignes incorrect. Attendu: {len(expected_lines)}, Obtenu: {len(actual_lines)}")
            return False
        
        # Vérifier chaque ligne (sauf le set qui peut avoir un ordre différent)
        success = True
        for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines)):
            if i == 2:  # Ligne du set - vérifier le contenu, pas l'ordre
                if "Hello" in actual and "Mulhouse!" in actual and actual.startswith("{") and actual.endswith("}"):
                    print(f"✅ Ligne {i+1}: Set correct (ordre peut varier)")
                else:
                    print(f"❌ Ligne {i+1}: Set incorrect")
                    success = False
            else:
                if expected == actual:
                    print(f"✅ Ligne {i+1}: Correct")
                else:
                    print(f"❌ Ligne {i+1}: Incorrect")
                    print(f"   Attendu: {expected}")
                    print(f"   Obtenu:  {actual}")
                    success = False
        
        if success:
            print("\n🎉 TOUS LES TESTS SONT PASSÉS!")
            return True
        else:
            print("\n❌ CERTAINS TESTS ONT ÉCHOUÉ")
            return False
            
    except Exception as error:
        print(f"❌ ERREUR lors de l'exécution du test: {error}")
        return False

if __name__ == "__main__":
    # Test fonctionnel
    print("\n=== TESTS FONCTIONNELS ===")
    functional_success = test_hello()
    
    # Résultat global
    print("\n=== RÉSUMÉ ===")
    if functional_success:
        print("✅ Fonctionnalité: Correcte")
    else:
        print("❌ Fonctionnalité: Incorrecte")

    sys.exit(0 if functionnal_success else 1)
