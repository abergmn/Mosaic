"""
port_scan.py

Module handling the functionality of the 'Discover hosts' menu option.
"""

from colorama import Fore

def host_discovery(target: str):
    """
    See docstring at the top of the document for information
    about this modules functionality...

    Args:

    Returns:

    """

    print(f"\n{Fore.CYAN}Running host discovery on '{target}'...")
    print(f"\n{Fore.CYAN}Finished host discovery on '{target}'.")
