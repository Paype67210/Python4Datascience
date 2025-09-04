import plotly.express as px
import pandas as pd
from load_csv import load

def main() -> None:
    """Affiche la projection de l'espérance de vie en fonction du PIB en 1900."""
    gdp_df = load("./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("./life_expectancy_years.csv")

    if gdp_df is None or life_df is None:
        print("Erreur : impossible de charger les fichiers CSV.")
        return

    # Nettoyage des colonnes
    gdp_df.columns = gdp_df.columns.str.strip()
    life_df.columns = life_df.columns.str.strip()

    try:
        # Extraction des données pour 1900
        gdp_1900 = gdp_df[["country", "1900"]].rename(columns={"1900": "gdp"})
        life_1900 = life_df[["country", "1900"]].rename(columns={"1900": "life_expectancy"})
    except KeyError as error:
        print(f"Error: Missing colomn in data - {error}.")
        return
            
    gdp_1900["gdp"] = pd.to_numeric(gdp_1900["gdp"], errors="coerce")
    life_1900["life_expectancy"] = pd.to_numeric(life_1900["life_expectancy"], errors="coerce")
    life_1900["life_expectancy"] = pd.to_numeric(life_1900["life_expectancy"], errors="coerce")

    merged_df = pd.merge(gdp_1900, life_1900, on="country").dropna()
    if merged_df.empty:
        print("Error: no valid datas for 1900!")
        return
        return

    # Tracé interactif avec Plotly
    fig = px.scatter(
        merged_df,
        x="gdp",
        y="life_expectancy",
        hover_name="country",
        title="Espérance de vie vs PIB par habitant en 1900",
        labels={
            "gdp": "PIB par habitant",
            "life_expectancy": "Espérance de vie (années)"
        }
    )
    fig.show()
        
if __name__ == "__main__":
    main()
