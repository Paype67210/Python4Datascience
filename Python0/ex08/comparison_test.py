#!/usr/bin/env python3
"""
Test de comparaison détaillée entre tqdm et ft_tqdm
"""

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

def test_comparison():
    """Test de comparaison détaillée"""
    
    print("=" * 60)
    print("COMPARAISON TQDM vs FT_TQDM")
    print("=" * 60)
    
    print("\n1. Test avec tqdm (original) :")
    print("-" * 40)
    for _ in tqdm(range(5), desc="tqdm"):
        sleep(0.3)
    
    print("\n2. Test avec ft_tqdm (clone) :")
    print("-" * 40)
    for _ in ft_tqdm(range(5)):
        sleep(0.3)
    
    print("\n" + "=" * 60)
    print("COMPARAISON TERMINÉE")
    print("=" * 60)

if __name__ == "__main__":
    test_comparison()
