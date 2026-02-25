"""
A small `pdoc` example.
"""

class Dog:
    """🐕"""
    name: str
    """The name of our dog."""
    friends: list["Dog"]
    """The friends of our dog."""

    def __init__(self, name: str):
        """Make a Dog without any friends (yet)."""
        self.name = name
        self.friends = []

    def bark(self, loud: bool = True):
        """*woof*"""

    def doggymaths(x, y):
        """
        You can even include tex based mathematical formulas

        Parameters:
        x: value x
        y: value y

        Returns:
        the value of $\\frac{x}{y}$
        """
        return x/y
