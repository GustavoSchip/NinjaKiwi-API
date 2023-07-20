#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest


@pytest.mark.asyncio
async def test_fetch_btd6():
    """Test for valid game and data types."""
    from ninjakiwi_api import fetch

    results = await fetch("BTD6", "races")
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("id")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btdb2():
    """Test for valid game and data types."""
    from ninjakiwi_api import fetch

    results = await fetch("BTDB2", "homs")
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("id")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_invalid_types():
    """Test for invalid game and data types."""
    from ninjakiwi_api import fetch

    results = await fetch("InvalidGame", "races")
    assert results is None

    results = await fetch("BTD6", "invalid_data_type")
    assert results is None

    results = await fetch("BTDB2", "invalid_data_type")
    assert results is None


@pytest.mark.asyncio
async def test_fetch_non_existent_data():
    """Test for non-existent data."""
    from ninjakiwi_api import fetch

    results = await fetch("BTD6", "non_existent_data")
    assert results is None

    results = await fetch("BTDB2", "non_existent_data")
    assert results is None


@pytest.mark.asyncio
async def test_fetch_with_options():
    """Test for valid game and data types with specific options."""
    from ninjakiwi_api import fetch

    options = {"userID": "example_user"}
    results = await fetch("BTDB2", "users", **options)
    assert results is not None

    options = {"homID": "example_hall_of_masters"}
    results = await fetch("BTDB2", "homs", **options)
    assert results is not None
