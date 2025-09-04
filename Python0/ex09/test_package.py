#!/usr/bin/env python3
"""
Script de test pour vérifier que le package ft_package répond aux exigences.
Ce script teste :
1. L'installation du package via pip
2. La présence dans pip list
3. Les informations avec pip show -v
4. L'importation et l'utilisation du module count_in_list
"""

import subprocess
import sys
import os
import tempfile
import venv

def run_command(cmd, shell=False):
    """Exécute une commande et retourne le résultat."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=shell)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def create_test_venv():
    """Crée un environnement virtuel temporaire pour les tests."""
    temp_dir = tempfile.mkdtemp()
    venv_path = os.path.join(temp_dir, "test_venv")
    venv.create(venv_path, with_pip=True)
    
    if os.name == 'nt':  # Windows
        pip_path = os.path.join(venv_path, "Scripts", "pip")
        python_path = os.path.join(venv_path, "Scripts", "python")
    else:  # Unix/Linux
        pip_path = os.path.join(venv_path, "bin", "pip")
        python_path = os.path.join(venv_path, "bin", "python")
    
    return temp_dir, venv_path, pip_path, python_path

def test_package_installation(dist_file, pip_path, python_path):
    """Teste l'installation et les fonctionnalités du package."""
    print(f"=== Test d'installation avec {os.path.basename(dist_file)} ===")
    
    # 1. Installation du package
    print("1. Installation du package...")
    code, stdout, stderr = run_command([pip_path, "install", dist_file])
    if code != 0:
        print(f"❌ Échec de l'installation: {stderr}")
        return False
    print("✅ Package installé avec succès")
    
    # 2. Vérification dans pip list
    print("\n2. Vérification dans pip list...")
    code, stdout, stderr = run_command([pip_path, "list"])
    if "ft-package" not in stdout.lower() and "ft_package" not in stdout.lower():
        print("❌ Package non trouvé dans pip list")
        print("Sortie de pip list:")
        print(stdout)
        return False
    print("✅ Package trouvé dans pip list")
    
    # 3. Vérification avec pip show -v
    print("\n3. Vérification avec pip show -v...")
    code, stdout, stderr = run_command([pip_path, "show", "-v", "ft_package"])
    if code != 0:
        print(f"❌ Échec de pip show: {stderr}")
        return False
    
    print("Sortie de pip show -v ft_package:")
    print(stdout)
    
    # Vérification des champs obligatoires
    required_fields = ["Name:", "Version:", "Summary:", "Author:", "License:", "Location:"]
    for field in required_fields:
        if field not in stdout:
            print(f"❌ Champ manquant: {field}")
            return False
    print("✅ Tous les champs obligatoires sont présents")
    
    # 4. Test de l'importation et de l'utilisation
    print("\n4. Test de l'importation et de l'utilisation...")
    test_script = '''
import sys
try:
    from ft_package import count_in_list
    
    # Test 1: compter "toto" dans ["toto", "tata", "toto"]
    result1 = count_in_list(["toto", "tata", "toto"], "toto")
    print(f"Test 1 - count_in_list(['toto', 'tata', 'toto'], 'toto'): {result1}")
    if result1 != 2:
        print("❌ Test 1 échoué - attendu: 2")
        sys.exit(1)
    
    # Test 2: compter "tutu" dans ["toto", "tata", "toto"]
    result2 = count_in_list(["toto", "tata", "toto"], "tutu")
    print(f"Test 2 - count_in_list(['toto', 'tata', 'toto'], 'tutu'): {result2}")
    if result2 != 0:
        print("❌ Test 2 échoué - attendu: 0")
        sys.exit(1)
    
    print("✅ Tous les tests de fonctionnalité ont réussi")
    
except ImportError as e:
    print(f"❌ Erreur d'importation: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erreur lors de l'exécution: {e}")
    sys.exit(1)
'''
    
    code, stdout, stderr = run_command([python_path, "-c", test_script])
    if code != 0:
        print(f"❌ Test de fonctionnalité échoué: {stderr}")
        print("Stdout:", stdout)
        return False
    
    print(stdout)
    print("✅ Test de fonctionnalité réussi")
    
    # 5. Désinstallation
    print("\n5. Désinstallation du package...")
    code, stdout, stderr = run_command([pip_path, "uninstall", "-y", "ft_package"])
    if code != 0:
        print(f"⚠️ Avertissement lors de la désinstallation: {stderr}")
    else:
        print("✅ Package désinstallé avec succès")
    
    return True

def main():
    """Fonction principale du test."""
    print("=== Script de test du package ft_package ===\n")
    
    # Vérification de l'existence des fichiers de distribution
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(current_dir, "dist")
    
    if not os.path.exists(dist_dir):
        print("❌ Répertoire dist/ non trouvé. Exécutez d'abord 'python -m build'")
        sys.exit(1)
    
    tar_file = os.path.join(dist_dir, "ft_package-0.0.1.tar.gz")
    wheel_file = os.path.join(dist_dir, "ft_package-0.0.1-py3-none-any.whl")
    
    if not os.path.exists(tar_file):
        print(f"❌ Fichier tar.gz non trouvé: {tar_file}")
        sys.exit(1)
    
    if not os.path.exists(wheel_file):
        print(f"❌ Fichier wheel non trouvé: {wheel_file}")
        sys.exit(1)
    
    print("✅ Fichiers de distribution trouvés")
    
    # Création d'un environnement virtuel de test
    print("\nCréation d'un environnement virtuel de test...")
    temp_dir, venv_path, pip_path, python_path = create_test_venv()
    print(f"✅ Environnement virtuel créé: {venv_path}")
    
    try:
        # Test avec le fichier tar.gz
        success_tar = test_package_installation(tar_file, pip_path, python_path)
        
        print("\n" + "="*60 + "\n")
        
        # Test avec le fichier wheel
        success_wheel = test_package_installation(wheel_file, pip_path, python_path)
        
        # Résultats finaux
        print("\n" + "="*60)
        print("=== RÉSULTATS FINAUX ===")
        print(f"Test avec tar.gz: {'✅ SUCCÈS' if success_tar else '❌ ÉCHEC'}")
        print(f"Test avec wheel: {'✅ SUCCÈS' if success_wheel else '❌ ÉCHEC'}")
        
        if success_tar and success_wheel:
            print("\n🎉 TOUS LES TESTS ONT RÉUSSI !")
            print("Votre package répond à toutes les exigences :")
            print("- ✅ Peut être installé via pip install ./dist/ft_package-0.0.1.tar.gz")
            print("- ✅ Peut être installé via pip install ./dist/ft_package-0.0.1-py3-none-any.whl")
            print("- ✅ Apparaît dans pip list")
            print("- ✅ Affiche les bonnes informations avec pip show -v")
            print("- ✅ La fonction count_in_list peut être importée et utilisée correctement")
        else:
            print("\n❌ CERTAINS TESTS ONT ÉCHOUÉ")
            sys.exit(1)
    
    finally:
        # Nettoyage
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"\n🧹 Environnement de test nettoyé")

if __name__ == "__main__":
    main()
