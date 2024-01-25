"""
Small utils to help with dicts
"""
import pandas as pd
import ast
from copy import deepcopy


def replace_value_if_key_in_2(d1: dict, d2: dict):
    """
    A util that replaces values in the first dict by the values
    in the second dict, only if the key is present there.

    Parameters
    ----------
    d1: dict
        Dictionary to be updated
    d2: dict
        Dictionary with new values

    Returns
    -------
    dict
    """
    assert isinstance(d1, dict) and isinstance(
        d2, dict
    ), "both inputs must be dictionaries"

    for key in d1.keys():
        if key in d2.keys():
            d1[key] = d2[key]
        else:
            pass
    return d1


def rename_key(d: dict, key_old: str, key_new: str):
    """
    Renames the key in the dictionary and returns
    an updated dict.

    Parameters
    ----------
    d
    key_old
    key_new

    Returns
    -------
    dict
    """
    assert not key_new in d, "Key {} already exists".format(key_new)
    if key_old in d:
        d[key_new] = deepcopy(d[key_old])
        del d[key_old]
    else:
        pass
    return d


def str_to_dict(string: str):
    """
    Convert string to dict, asserting that there are no nans to ensure
    correct parsing. Does not work when the str contains
    lists or tuples.

    NB: Something like np.nan cannot be a value and should be
    replaced by None, and then convert afterward!
    """
    assert (
        string.find("nan") < 0
    ), "cannot handle nan or np.nan; must be converted to None first and converted back afterward"
    return ast.literal_eval(string)


def dict_to_str_formatted(d: dict, indent: int = 3):
    """
    This util converts a dict to a formatted string
    that can be printed and is easy to read
    """
    str_indents = " " * indent
    string = (
        d.__str__()[:-1]
        .replace(", ", f"\n{str_indents}")
        .replace("{", str_indents)
        .replace("'", "")
    )
    return string


def dict_first_val(d: dict):
    """
    Returns the value of the first key of the input dict
    """
    return d[list(d.keys())[0]]


def dict_to_kwarg_str(d: dict):
    """
    Converts a dict to a kwarg string that can be passed using
    the execute parsing
    """
    ls = []
    for key, value in d.items():
        if isinstance(value, str):
            ls.append(f"{key}='{value}'")
        else:
            ls.append(f"{key}={value}")

    return ", ".join(ls)


def excel_to_dict(file: str):
    """
    Convert an Excel file with two columns to a dict:
        column 1: key
        column 2: value (automatically tries to parse using
            ast.literal_eval, otherwise value is kept)
    The util has its limitations: lists are usually not
    parsed correctly.
    """
    # read Excel file and get
    df = pd.read_excel(file, index_col=0).reset_index()
    colnames = df.columns
    assert len(colnames) == 2, "input excel file does not have 2 columns"
    df = df.rename(columns={colnames[0]: "key", colnames[1]: "value"}).set_index("key")
    # convert to dictionary
    d = df.to_dict(orient="dict")["value"]
    # parse values that are strings
    for key in d:
        if isinstance(d[key], str):
            try:
                d[key] = ast.literal_eval(d[key])
            except (ValueError, SyntaxError):
                pass
        else:
            continue
    return d

