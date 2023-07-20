"""Top-level package for NinjaKiwi API."""

__author__ = """Gustavo Schip"""
__email__ = "gustavoschip@proton.me"
__version__ = "0.0.1"

from .FUNCTIONS import _error_handler
from .main import *

__all__ = [
    "fetch",
]
