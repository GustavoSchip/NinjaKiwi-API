"""API-level package for NinjaKiwi API."""

from .BTD6 import _btd6_url_factory
from .BTDB2 import _btdb2_url_factory

__all__ = [
    "_btd6_url_factory",
    "_btdb2_url_factory",
]
