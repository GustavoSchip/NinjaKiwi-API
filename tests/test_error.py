#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest

from ninjakiwi_api.FUNCTIONS import _error_handler


@pytest.mark.asyncio
async def test_http_error_401():
    """Test for HTTP 401 Unauthorized error."""
    pass  # TODO : Implement


@pytest.mark.asyncio
async def test_http_error_404():
    """Test for HTTP 404 Not Found error."""
    pass  # TODO : Implement


@pytest.mark.asyncio
async def test_http_error_unknown():
    """Test for unknown HTTP error."""
    pass  # TODO : Implement


@pytest.mark.asyncio
async def test_str_error():
    """Test for a custom string error."""
    error_message = "Custom error message"

    with pytest.raises(Warning) as warning:
        await _error_handler("str", exception=error_message)

    assert str(warning.value) == error_message
