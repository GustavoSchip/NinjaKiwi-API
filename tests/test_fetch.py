#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest
from os import environ

from ninjakiwi_api import fetch


@pytest.mark.asyncio
async def test_fetch_btd6():
    """Test for valid game and data types."""
    results = await fetch("BTD6", "races")
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("id")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btdb2():
    """Test for valid game and data types."""
    results = await fetch("BTDB2", "homs")
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("id")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btd6_bosses():
    """Test fetching boss data for BTD6."""
    options = {"teamSize": "1"}
    results = await fetch("BTD6", "bosses", **options)
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("id")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btd6_challenges():
    """Test fetching challenge data for BTD6."""
    options = {"challengeFilter": "newest"}
    results = await fetch("BTD6", "challenges", **options)
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("type")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btd6_odyssey():
    """Test fetching Odyssey event data for BTD6."""
    results = await fetch("BTD6", "odyssey")
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("id")
    assert temp is not None


@pytest.mark.asyncio
@pytest.mark.skipif(
    not environ.get("PYTEST_BTD6_USER_ID"),
    reason="PYTEST_BTD6_USER_ID environment variable not found",
)
async def test_fetch_btdb2_users():
    """Test fetching user data for BTDB2."""
    options = {
        "userID": str(environ.get("PYTEST_BTD6_USER_ID")),
    }
    results = await fetch("BTDB2", "users", **options)
    assert results is not None

    data = await results.get_raw_data()
    assert "success" in data

    temp = await results.get_data("name")
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_invalid_types():
    """Test for invalid game and data types."""
    results = await fetch("InvalidGame", "races")
    assert results is None

    results = await fetch("BTD6", "invalid_data_type")
    assert results is None

    results = await fetch("BTDB2", "invalid_data_type")
    assert results is None


@pytest.mark.asyncio
async def test_fetch_non_existent_data():
    """Test for non-existent data."""
    results = await fetch("BTD6", "non_existent_data")
    assert results is None

    results = await fetch("BTDB2", "non_existent_data")
    assert results is None


@pytest.mark.asyncio
@pytest.mark.skipif(
    not environ.get("PYTEST_BTD6_USER_ID"),
    reason="PYTEST_BTD6_USER_ID environment variable not found",
)
async def test_fetch_with_options():
    """Test for valid game and data types with specific options."""
    options = {"userID": str(environ.get("PYTEST_BTD6_USER_ID"))}
    results = await fetch("BTDB2", "users", **options)
    assert results is not None

    temp = await fetch("BTDB2", "homs")
    homid = await temp.get_homid(number=1)

    options = {"homID": str(homid)}
    results = await fetch("BTDB2", "homs", **options)
    assert results is not None
