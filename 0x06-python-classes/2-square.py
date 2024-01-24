#!/usr/bin/python3
"""Define a class Square with private attribute size."""

class Square:
    """Represent a square.

    Attributes:
        __size (int): Size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square Class.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
