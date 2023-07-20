#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
from os import environ

# pylint: disable=redefined-outer-name

import pytest


@pytest.mark.asyncio
async def test_fetch_btd6():
    """Test for valid game and data types."""
    from ninjakiwi_api import fetch

    results = await fetch("BTD6", "races")
    print(results)
    assert results is not None

    data = await results.get_raw_data()
    print(data)
    assert "success" in data

    temp = await results.get_data("id")
    print(temp)
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btdb2():
    """Test for valid game and data types."""
    from ninjakiwi_api import fetch

    results = await fetch("BTDB2", "homs")
    print(results)
    assert results is not None

    data = await results.get_raw_data()
    print(data)
    assert "success" in data

    temp = await results.get_data("id")
    print(temp)
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btd6_bosses():
    """Test fetching boss data for BTD6."""
    from ninjakiwi_api import fetch

    options = {"teamSize": "1"}
    results = await fetch("BTD6", "bosses", **options)
    print(results)
    assert results is not None

    data = await results.get_raw_data()
    print(data)
    assert "success" in data

    temp = await results.get_data("id")
    print(temp)
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btd6_challenges():
    """Test fetching challenge data for BTD6."""
    from ninjakiwi_api import fetch

    options = {"challengeFilter": "newest"}
    results = await fetch("BTD6", "challenges", **options)
    print(results)
    assert results is not None

    data = await results.get_raw_data()
    print(data)
    assert "success" in data

    temp = await results.get_data("type")
    print(temp)
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btd6_odyssey():
    """Test fetching Odyssey event data for BTD6."""
    from ninjakiwi_api import fetch

    options = {"odysseyID": "example_odyssey", "difficulty": "easy", "maps": True}
    results = await fetch("BTD6", "odyssey", **options)
    print(results)
    assert results is not None

    data = await results.get_raw_data()
    print(data)
    assert "success" in data

    temp = await results.get_data("id")
    print(temp)
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_btdb2_users():
    """Test fetching user data for BTDB2."""
    from ninjakiwi_api import fetch

    options = {
        "userID": str(environ.get("PYTEST_BTD6_USER_ID")),
    }
    results = await fetch("BTDB2", "users", **options)
    print(results)
    assert results is not None

    data = await results.get_raw_data()
    print(data)
    assert "success" in data

    temp = await results.get_data("name")
    print(temp)
    assert temp is not None


@pytest.mark.asyncio
async def test_fetch_invalid_types():
    """Test for invalid game and data types."""
    from ninjakiwi_api import fetch

    results = await fetch("InvalidGame", "races")
    print(results)
    assert results is None

    results = await fetch("BTD6", "invalid_data_type")
    print(results)
    assert results is None

    results = await fetch("BTDB2", "invalid_data_type")
    print(results)
    assert results is None


@pytest.mark.asyncio
async def test_fetch_non_existent_data():
    """Test for non-existent data."""
    from ninjakiwi_api import fetch

    results = await fetch("BTD6", "non_existent_data")
    print(results)
    assert results is None

    results = await fetch("BTDB2", "non_existent_data")
    print(results)
    assert results is None


@pytest.mark.asyncio
async def test_fetch_with_options():
    """Test for valid game and data types with specific options."""
    from ninjakiwi_api import fetch

    options = {"userID": "example_user"}
    results = await fetch("BTDB2", "users", **options)
    print(results)
    assert results is not None

    options = {"homID": "example_hall_of_masters"}
    results = await fetch("BTDB2", "homs", **options)
    print(results)
    assert results is not None
