#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest
from aiohttp import test_utils

from ninjakiwi_api.FUNCTIONS import _error_handler


@pytest.mark.asyncio
async def test_http_error_200():
    """Test for HTTP 200 status code."""
    response_json = {"error": "Some error message"}

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=response_json)
    request.status = 200

    with pytest.raises(Warning) as warning:
        await _error_handler("http", response=request)

    assert str(warning.value) == "Some error message"


@pytest.mark.asyncio
async def test_http_error_404():
    """Test for HTTP 404 status code."""
    response_json = {"error": "Some error message"}

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=response_json)
    request.read = test_utils.make_mocked_coro(return_value=response_json)
    request.status = 404

    with pytest.raises(Warning) as warning:
        await _error_handler("http", response=request)

    assert str(warning.value) == str(response_json)


@pytest.mark.asyncio
async def test_http_error_500():
    """Test for HTTP 500 status code."""
    response_json = {"error": "Some error message"}

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=response_json)
    request.read = test_utils.make_mocked_coro(return_value=response_json)
    request.status = 500

    with pytest.raises(Warning) as warning:
        await _error_handler("http", response=request)

    assert str(warning.value) == str(response_json)


@pytest.mark.asyncio
async def test_http_error_unknown():
    """Test for unknown HTTP status code."""
    response_json = {"error": "Some error message"}

    request = test_utils.make_mocked_request("GET", "/test", headers={})
    request.json = test_utils.make_mocked_coro(return_value=response_json)
    request.status = 400

    with pytest.raises(Exception) as warning:
        await _error_handler("http", response=request)

    assert str(warning.value) == "Not a valid HTTP status!"


@pytest.mark.asyncio
async def test_http_error_no_response():
    """Test for no HTTP response."""
    with pytest.raises(Exception, match="Not a valid HTTP response!"):
        await _error_handler("http")


@pytest.mark.asyncio
async def test_str_error():
    """Test for string error."""
    with pytest.raises(Warning) as warning:
        await _error_handler("str", exception="Custom exception message")

    assert str(warning.value) == "Custom exception message"


@pytest.mark.asyncio
async def test_str_error_no_exception():
    """Test for missing string error exception."""
    with pytest.raises(Exception, match="Not a valid exception!"):
        await _error_handler("str")


@pytest.mark.asyncio
async def test_invalid_action():
    """Test for invalid action."""
    with pytest.raises(Exception, match="Not a valid action!"):
        await _error_handler("invalid_action")


@pytest.mark.asyncio
async def test_missing_http_response():
    """Test for missing HTTP response."""
    with pytest.raises(Exception, match="Not a valid HTTP response!"):
        await _error_handler("http", response=None)


@pytest.mark.asyncio
async def test_invalid_str_exception():
    """Test for invalid string exception."""
    with pytest.raises(Exception, match="Not a valid exception!"):
        await _error_handler("str", exception=123)
