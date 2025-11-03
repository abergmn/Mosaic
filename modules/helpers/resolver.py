"""
resolver.py

Helper for resolving a user-provided target (IP or hostname)
into a canonical IP address.
"""

def resolve_target(target: str) -> str:
    """
    Resolve hostname or IPv4 string to IPv4 address.

    Args:
        target (str): An IP address or hostname.

    Returns:
        str: The resolved canonical IP address.

    Raises:
        ValueError: If the target cannot be resolved.
    """

    return
