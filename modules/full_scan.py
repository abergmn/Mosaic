"""
port_scan.py

Module handling the functionality of the 'Full scan (hosts + ports + banners)' menu option.
"""

from colorama import Fore

def full_scan(target: str):
    """
    See docstring at the top of the document for information
    about this modules functionality...

    Args:
        target (str):

    Returns:

    """

    print(f"\n{Fore.CYAN}Running full scan on '{target}'...")
    print(f"\n{Fore.CYAN}Finished full scan on '{target}'.")
