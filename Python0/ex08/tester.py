"""
Tester.py - Script de test pour comparer la fonction ft_tqdm à tqdm.

Ce script :
- Importe ft_tqdm depuis Loading.py
- Compare visuellement les barres de progression ft_tqdm et tqdm
- Vérifie la conformité flake8
"""

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

def test_progress_bars() -> None:
    """
    Affiche deux barres de progression :
    - Une avec tqdm (librairie standard)
    - Une avec ft_tqdm (implémentation personnalisée)
    """
    print("Test avec tqdm :")
    for _ in tqdm(range(10)):
        sleep(0.1)

    print("\nTest avec ft_tqdm :")
    for _ in ft_tqdm(range(10)):
        sleep(0.1)


if __name__ == "__main__":
    test_progress_bars()
