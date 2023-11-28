#!/usr/bin/python3
"""
Locked class
"""


class LockedClass:
    """
    Prevents user from creating a new instance dynamically
    """
    __slots__ = ('first_name',)
