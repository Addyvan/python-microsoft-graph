"""
Queries for microsoft graph
Written by: Addyvan + Jess Gilchrist
"""

from .users import *
from .groups import *
from .reports import *
from .teams import *
from .directory import *

__all__ = ["users", "groups", "reports", "teams", "directory"]