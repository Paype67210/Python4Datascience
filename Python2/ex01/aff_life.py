import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
import sys


def plot_life_expectancy(country: str, data: pd.DataFrame) -> None:
    """
    Plot the life expectancy data for a specific country using matplotlib.

    Args:
        country (str): The country for which to plot the data.
        data (pd.DataFrame): DataFrame containing the life expectancy data.

    Raises:
        KeyError: If there is no Country Colomn in the dataset.
        ValueError: If the country is not found in the dataset.
        Exception: For any other plotting errors.
    """

    try:
        # Check if country exists in the dataset
        if country not in data['country'].values:
            raise KeyError(f"Country '{country}' not found in the dataset")

        # Filter data for the specific country
        country_data = data[data['country'] == country]

        # Check if we have data for this country
        if country_data.empty:
            raise ValueError(f"No data available for country '{country}'")

        # Prepare data for plotting (transpose and convert years to columns)
        years = data.columns[1:].astype(int)
        life_expectancy_values = country_data.iloc[0, 1:].values

        # Convert to numeric, handling missing values
        life_expectancy_values = pd.to_numeric(life_expectancy_values,
                                               errors='coerce')

        # Create the plot
        plt.figure(figsize=(12, 8))
        plt.plot(years, life_expectancy_values, linewidth=2, label=country)

        # Adding title and labels
        plt.title(f'{country} Life expectancy Projections', fontsize=16, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Life expectancy', fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)

        # Format x-axis to show years nicely
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    except ValueError as vError:
        print(f"ValueError: {vError}", file=sys.stderr)
        raise
    except KeyError as kError:
        print(f"KeyError: Missing expected column in dataset - {kError}", file=sys.stderr)
        raise
    except Exception as error:
        print(f"Unexpected error while plotting: {error}", file=sys.stderr)
        raise


def main() -> None:
    """
    Main function to load data and plot life expectancy for France.

    Handles various exceptions that might occur during execution.
    """

    try:
        # Load the dataset
        data = load('life_expectancy_years.csv')

        if data is None:
            print("Error: Failed to load the dataset. Please check the file path and format.", file=sys.stderr)
            return

        # Validate that we have the expected structure
        if data.empty:
            print("Error: The loaded dataset is empty.", file=sys.stderr)
            return

        if 'country' not in data.columns:
            print("Error: The dataset doesn't contain a 'country' column.", file=sys.stderr)
            return

        # Plot life expectancy for France (42 Mulhouse is a campus in France)
        plot_life_expectancy('France', data)

    except FileNotFoundError:
        print("Error: The file 'life_expectancy_years.csv' was not found.", file=sys.stderr)
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty or contains no data.", file=sys.stderr)
    except pd.errors.ParserError as pe:
        print(f"Error: Failed to parse the CSV file - {pe}", file=sys.stderr)
    except ValueError as vError:
        print(f"Error: {vError}", file=sys.stderr)
    except KeyError as kError:
        print(f"Error: Missing expected data structure - {kError}", file=sys.stderr)
    except ImportError as iError:
        print(f"Error: Missing required library - {iError}", file=sys.stderr)
    except Exception as error:
        print(f"Unexpected error occurred: {error}", file=sys.stderr)
        print("Please check your data file and try again.")
    finally:
        # Clean up if needed (e.g., close files, clear memory)
        pass


if __name__ == "__main__":
    main()
