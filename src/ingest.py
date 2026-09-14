"""
Ingest module — load and clean price data from CSVs.

>>> Partner A owns this module. <<<

Every function below has:
  - a docstring saying WHAT the function should do (the contract)
  - a series of  # TODO  comments saying HOW to do it, step by step
  - a  raise NotImplementedError  as a placeholder — delete it when done

Your job: replace the NotImplementedError with real code, following the TODOs.

You are DONE with this module when this command runs green:

    pytest tests/test_ingest.py -v

Do not edit tests/test_ingest.py — that file defines what "correct" means.
"""

from pathlib import Path
import pandas as pd


def load_prices(path):
    """
    Load ONE price CSV and return a tidy DataFrame.

    The input CSV has 2 columns:
        date   (string, YYYY-MM-DD)
        close  (float)

    Your job: return a DataFrame with 3 columns, IN THIS ORDER:
        date    (datetime, NOT string)
        ticker  (string, taken from the filename without the .csv extension,
                 always LOWERCASE — e.g. 'data/raw/AAPL.csv' → 'aapl')
        close   (float)

    Example:
        >>> df = load_prices('data/raw/aapl.csv')
        >>> list(df.columns)
        ['date', 'ticker', 'close']
        >>> df['ticker'].iloc[0]
        'aapl'

    Parameters
    ----------
    path : str or pathlib.Path
        Path to a single CSV file.

    Returns
    -------
    pandas.DataFrame
    """
    path = Path(path)

    df = pd.read_csv(path, parse_dates=['date'])

    df['ticker'] = path.stem.lower()

    return df[['date', 'ticker', 'close']]


def clean_prices(df):
    """
    Clean a price DataFrame.

    Steps, in order:
      1. Drop rows where  close  is NaN
      2. Sort by  date  ascending
      3. Drop exact duplicate rows
      4. Reset the index (so rows become 0, 1, 2, ...)

    The function must NOT modify the input — return a new DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Any DataFrame with a  close  column.

    Returns
    -------
    pandas.DataFrame
    """
    return (df.dropna(subset=['close'])
              .sort_values('date')
              .drop_duplicates()
              .reset_index(drop=True))


def load_all_prices(folder):
    """
    Load every  *.csv  file in  folder , combine them into ONE DataFrame,
    then clean the result.

    Parameters
    ----------
    folder : str or pathlib.Path
        Folder containing per-ticker CSVs (aapl.csv, msft.csv, ...).

    Returns
    -------
    pandas.DataFrame
        All prices concatenated and cleaned.

    Raises
    ------
    FileNotFoundError
        If  folder  does not exist OR contains no  .csv  files.
    """
    folder = Path(folder)

    if not folder.is_dir():
        raise FileNotFoundError(f"folder not found: {folder}")

    csv_files = list(folder.glob('*.csv'))
    if not csv_files:
        raise FileNotFoundError(f"no .csv files found in: {folder}")

    dfs = []
    for f in csv_files:
        dfs.append(load_prices(f))

    combined = pd.concat(dfs, ignore_index=True)

    return clean_prices(combined)
