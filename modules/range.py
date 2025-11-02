"""
range.py

Module for generating a list of IP addresses to scan
based on a single IP or CIDR notation.
"""

from typing import List

def find_range(cidr_ip: str) -> List[str]:
    """
    Generate a list of IP addresses from a CIDR range.

    Args:
        cidr_ip (str): A string representing an IP range in CIDR notation 
                       (e.g., '192.168.1.0/24').

    Returns:
        List[str]: A list of IP addresses within the specified range.
    """

    return
