from load_csv import load


if __name__ == "__main__":
    data = load("./life_expectancy_years.csv")
    if data is not None:
        print(data.head())  # Affiche 1ères lignes pour vérification
