#!/usr/bin/python3
"""
Locked class
"""


class LockedClass:
    """
    Prevents user from creating a new instance dynamically
    """
    ___slots__ = ('first_name',)
