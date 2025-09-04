# Format_ft_time.py

from datetime import datetime
import time
# Obtenir le timestamp actuel
now = time.time()
now_date = datetime.now()

# Affichage du timestamp avec 4 décimales et en notation scientifique
print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")

# Affichage de la date formatée
print(now_date.strftime("%b %d %Y"))
