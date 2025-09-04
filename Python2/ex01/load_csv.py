import pandas as pd
from typing import Optional


def load(path: str) -> Optional[pd.DataFrame]:
    """
    Loads a CSV file and prints its dimensions.

    Args:
        path (str): Path to the CSV file.

    Returns:
        Optional[pd.DataFrame]: DataFrame or None if an error occurs.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except (FileNotFoundError,
            pd.errors.EmptyDataError,
            pd.errors.ParserError) as error:
        print(f"Error loading dataset: {error}")
        return None
