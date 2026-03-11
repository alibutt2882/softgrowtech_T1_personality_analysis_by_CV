# pages/__init__.py
"""
Pages package for CV Personality Analyzer
This file makes Python treat the directory as a package
"""

from . import dashboard
from . import history
from . import settings
from . import about

__all__ = ['dashboard', 'history', 'settings', 'about']
