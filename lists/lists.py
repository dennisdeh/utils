from typing import Union
from collections.abc import KeysView

"""
Small utils to help with lists
"""


def remove_duplicates(l1: Union[list, KeysView]):
    """
    Gives a list without duplicates.
    """
    return list(set(l1))


def intersection(l1: Union[list, KeysView], l2: Union[list, KeysView]):
    """
    Gives a list containing only the elements in common
    between the two input lists.
    """
    return list(set(l1).intersection(l2))


def difference(l1: Union[list, KeysView], l2: Union[list, KeysView]):
    """
    Gives a list containing the elements of l1
    not in l2.
    """
    return list(set(l1).difference(l2))


def union(l1: Union[list, KeysView], l2: Union[list, KeysView]):
    """
    Gives a list containing the elements of l1
    and l2, without overlap.
    """
    return list(set(l1).union(l2))


def is_sublist(l1: Union[list, KeysView], l2: Union[list, KeysView]):
    """
    Returns a bool whether all elements of l1
    are contained in l2.
    An empty list is always a sublist of another
    empty or non-empty list.
    """
    if len(l1) == 0 or len(l2) == 0:
        return True
    else:
        return len(intersection(l1, l2)) == len(list(set(l1)))


def has_same_elements(l1: Union[list, KeysView], l2: Union[list, KeysView]):
    """
    Returns a bool whether all elements in l1
    are contained in l2 and nothing more.
    If both lists are empty True is returned.
    """
    if len(l1) == 0:
        if len(l2) == 0:
            return True
        else:
            return False
    elif len(l2) == 0:
        if len(l1) == 0:
            return True
        else:
            return False
    else:
        return is_sublist(l1, l2) and is_sublist(l2, l1)
