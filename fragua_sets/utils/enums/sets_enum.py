"""Sets Enum."""

from enum import Enum


class Sets(str, Enum):
    """Sets enum class."""

    UTILITY = "utility"
    EXTRACTION = "extraction"
    LOAD = "load"
    PIPELINES = "pipelines"
