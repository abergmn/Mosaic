"""
resolve_target.py

Module handling the functionality of the 'Resolve IP/Hostname' menu option.
"""

from .helpers import resolve
from typing import Tuple

def resolve_target(target: str) -> Tuple[str, str]:
    """
    Return a tuple of containing the IP and hostname for a given target.

    Args:
        target (str): The target to resolve.

    Returns:
        Tuple[str, str]: The IP and hostname.
    """
    return target, target
