"""Utility functions and enums for algorithms."""

from enum import Enum


class EdgesIndex(Enum):
    """Enum to represent the index of edges in a tuple."""

    WEIGHT = 0
    FROM_NODE = 1
    TO_NODE = 2
