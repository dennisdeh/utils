import pandas as pd
from itertools import chain
from typing import Union


def filter_target(df,
                  target_col: str,
                  list_substrings: Union[list, None] = None):
    """
    A little util to prepare a target column for subsequent
    steps in the preparation of development/validation data.

    Choose target and drop remaining columns containing
    substrings in list_substrings. This is convenient if
    several candidate target columns are present in df.

    The chosen column will be renamed "target" and nans
    are dropped.

    Parameters
    ----------
    df: pd.DataFrame
        The input data frame.
    target_col: str
        Name of target column to keep.
    list_substrings: list or None
        List of substrings that the columns to be dropped
        contains in their name. If None, no columns will be
        dropped

    Returns
    -------
    pd.DataFrame
    """
    # 1: initialisation
    # prepare list of substrings to drop
    if list_substrings is None:
        list_substrings = []
    elif isinstance(list_substrings, list):
        pass
    else:
        raise ValueError("Invalid input for list_substrings")
    # assertions
    assert isinstance(df, pd.DataFrame)
    assert target_col in df.columns, "target_col must be a column in df"

    # 2: construct list of columns to drop if they contain one of the substrings in list_substrings
    cols_to_exclude = []
    for substring in list_substrings:
        cols_to_exclude.append(list(filter(lambda x: substring in x, df.columns)))
    # flatten list and remove target column from list of columns to be dropped
    target_cols = list(chain(*cols_to_exclude))
    if len(target_cols) == 0:
        pass
    else:
        target_cols.remove(target_col)
        df = df.drop(target_cols, axis=1)

    # 3: final step
    # rename target column for simplicity
    df = df.rename({target_col: "target"}, axis=1)
    # drop nans in target column
    df = df[~df["target"].isna()]
    return df
