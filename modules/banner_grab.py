"""
port_scan.py

Module handling the functionality of the 'Banner grabbing only' menu option.
"""

from colorama import Fore

def banner_grab(target: str):
    """
    See docstring at the top of the document for information
    about this modules functionality...

    Args:
        target (str): IP address or hostname

    Returns:

    """

    print(f"\n{Fore.CYAN}Running banner grabbing on '{target}'...")
    print(f"\n{Fore.CYAN}Finished banner grab on '{target}'.")
