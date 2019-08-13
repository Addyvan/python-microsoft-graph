"""
Queries for microsoft graph
Written by: Addyvan + Jess Gilchrist
"""

from .users import *
from .groups import *
from .reports import *
from .teams import *

__all__ = ["users", "groups", "reports", "teams"]