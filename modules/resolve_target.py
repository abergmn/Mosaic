"""
resolve_target.py

Module handling the functionality of the 'Resolve IP/Hostname' menu option.
Return a tuple containing the IP and hostname for a given target.
"""

from .helpers import resolve
from typing import Tuple

def resolve_target(target: str) -> Tuple[str, str] | Tuple[None, None]:
    """
    See docstring at the top of the document for information
    about this modules functionality...

    Args:
        target (str): The target to resolve.

    Returns:
        Tuple[str, str]: The IP and hostname.
    """

    # determine if hostname, if hostname, lookup ip
    # if ip, if ip, lookup hostname
    # if neither, ...

    return target, target
