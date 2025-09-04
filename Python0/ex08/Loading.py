import time
import sys
from typing import Generator, Any


def ft_tqdm(lst: range) -> Generator[Any, None, None]:
    """
    Clone parfait de tqdm avec toutes ses fonctionnalités.
    """
    total = len(lst)
    bar_length = 42  # Longueur exacte pour matcher tqdm
    start_time = time.time()
    
    for i, item in enumerate(lst):
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        # Calculer le pourcentage de progression
        progress = (i + 1) / total
        percentage = int(progress * 100)
        
        # Calculer le nombre de blocs remplis dans la barre
        filled_length = int(bar_length * progress)
        
        # Créer la barre de progression (exactement comme tqdm)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        
        # Calculer la vitesse (items par seconde)
        if elapsed_time > 0:
            rate = (i + 1) / elapsed_time
        else:
            rate = 0
        
        # Calculer le temps restant estimé
        if rate > 0 and i > 0:
            eta = (total - i - 1) / rate
            eta_str = format_time(eta)
        else:
            eta_str = "?"
        
        # Formater le temps écoulé
        elapsed_str = format_time(elapsed_time)
        
        # Construire la chaîne de progression exactement comme tqdm
        if i == 0 and elapsed_time < 0.01:  # Premier affichage
            rate_str = "?it/s"
        else:
            rate_str = f"{rate:.2f}it/s"
        
        # Format final identique à tqdm
        progress_str = f'\r{percentage:3d}%|{bar}| {i + 1}/{total} [{elapsed_str}<{eta_str}, {rate_str}]'
        
        # Afficher la barre de progression
        print(progress_str, end='', flush=True)
        
        # Yield l'élément actuel
        yield item
    
    # Affichage final (identique à tqdm)
    final_time = time.time() - start_time
    final_rate = total / final_time if final_time > 0 else 0
    final_time_str = format_time(final_time)
    final_rate_str = f"{final_rate:.2f}it/s"
    
    final_bar = '█' * bar_length
    final_str = f'\r100%|{final_bar}| {total}/{total} [{final_time_str}<00:00, {final_rate_str}]'
    print(final_str)
    print()  # Nouvelle ligne finale


def format_time(seconds: float) -> str:
    """
    Formate le temps en format MM:SS comme tqdm.
    """
    if seconds == float('inf') or seconds != seconds:  # inf ou nan
        return "?"
    
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    
    return f"{minutes:02d}:{secs:02d}"
