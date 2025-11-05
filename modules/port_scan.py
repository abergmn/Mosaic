"""
port_scan.py

Module handling the functionality of the 'Port scan' menu option.
"""

from colorama import Fore

def port_scan(target: str):
    """
    See docstring at the top of the document for information
    about this modules functionality...

    Args:
        

    Returns:

    """

    print(f"\n{Fore.CYAN}Running port scan on '{target}'...")
    print(f"\n{Fore.CYAN}Finished port scan on '{target}'.")
