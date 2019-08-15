"""
Queries for microsoft graph
Written by: Addyvan + Jess Gilchrist
"""

from .users import *
from .groups import *
from .jess_groups import *
from .reports import *
from .teams import *
from .directory import *
from .sites import *

__all__ = ["users", "groups", "reports", "teams", "directory", "sites", "jess_groups"]