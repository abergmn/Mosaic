"""
port_scan.py

Helper for scanning a list of TCP ports on a given host
and returning which ports are open.
"""

from typing import List

def scan_ports(ip: str, ports: List[int]) -> List[int]:
    """
    Scan the specified ports on a host and return the open ports.

    Args:
        ip (str): The target IP address.
        ports (List[int]): A list of TCP ports to scan.

    Returns:
        List[int]: A list of ports that are open on the host.
    """

    return
