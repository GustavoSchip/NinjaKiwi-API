"""FUNCTION-level package for NinjaKiwi API."""

from .ERROR import _error_handler
from .FETCH import _api_fetch

__all__ = ["_api_fetch", "_error_handler"]
