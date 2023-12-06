#!/usr/bin/python3
"""
My integer
"""


class MyInt(int):
    """
    A class representing MyInt that inherits from int.

    MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__ne__(other)
