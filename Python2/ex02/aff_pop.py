import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load
import sys

def convert_population_string(pop_str: str) -> float:
    """
    Convertit les chaînes de population avec suffixes (M, k) en nombres.
    """
    if isinstance(pop_str, (int, float)):
        return float(pop_str)
    
    pop_str = str(pop_str).strip()
    
    if pop_str.endswith('M'):
        return float(pop_str[:-1]) * 1_000_000
    elif pop_str.endswith('k'):
        return float(pop_str[:-1]) * 1_000
    else:
        return float(pop_str)

def plot_population_comparison(country1: str, country2: str, years: list, data: pd.DataFrame) -> None:
    """
    Affiche sur le même graphique la population de deux pays, pour les années données.
    """
    try:
        for country in [country1, country2]:
            if country not in data['country'].values:
                raise KeyError(f"Country '{country}' not found in the dataset")

        country1_data = data[data['country'] == country1].iloc[0]
        country2_data = data[data['country'] == country2].iloc[0]

        # Extraction des colonnes années
        available_years = [int(col) for col in data.columns if col != 'country']
        # On garde seulement les années souhaitées
        selected_years = [str(year) for year in years if year in available_years]

        # Conversion des valeurs de population avec gestion des suffixes M et k
        pop1 = [convert_population_string(country1_data[year]) for year in selected_years]
        pop2 = [convert_population_string(country2_data[year]) for year in selected_years]

        plt.figure(figsize=(12, 8))
        plt.plot(years, pop1, label=country1, linewidth=2)
        plt.plot(years, pop2, label=country2, linewidth=2)

        plt.title(f'Population comparison: {country1} vs {country2} (1800-2050)', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Population', fontsize=12)
        
        # Formatage de l'axe Y pour afficher les nombres en millions
        plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x/1e6:.1f}M'))
        
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    except KeyError as kError:
        print(f"KeyError: {kError}", file=sys.stderr)
    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)

def main():
    try:
        data = load('./population_total.csv')
        if data is None or data.empty:
            print("Error: Failed to load the dataset or it's empty.", file=sys.stderr)
            return
        if 'country' not in data.columns:
            print("Error: The dataset doesn't contain a 'country' column.", file=sys.stderr)
            return

        country1 = "France"      # Pays de 42 Mulhouse
        country2 = "Australia"   # Pays des Kangourous
        years = list(range(1800, 2051))

        plot_population_comparison(country1, country2, years, data)

    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)

if __name__ == "__main__":
    main()
