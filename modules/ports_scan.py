"""
port_scan.py

Module handling the functionality of the 'Port(s) scan' menu option.
"""

from colorama import Fore

def port_scan(target: str):
    """
    See docstring at the top of the document for information
    about this modules functionality...

    Args:
        target (str): Hello, World!

    Returns:

    """

    print(f"\n{Fore.CYAN}Running port(s) scan on '{target}'...")
    print(f"\n{Fore.CYAN}Finished port(s) scan on '{target}'.")
