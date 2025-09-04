#!/usr/bin/env python3

import time
import sys
from tqdm import tqdm

def analyze_tqdm_format():
    """Analyse le format exact de tqdm"""
    
    print("=== ANALYSE DU FORMAT TQDM ===")
    
    # Test avec une itération très lente pour voir le format
    items = range(5)
    
    for i in tqdm(items, desc="Progress", ncols=80):
        time.sleep(0.5)  # Plus lent pour mieux voir
    
    print("\n=== ANALYSE TERMINÉE ===")

if __name__ == "__main__":
    analyze_tqdm_format()
