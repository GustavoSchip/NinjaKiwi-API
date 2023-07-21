#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest

from ninjakiwi_api.API import _btdb2_url_factory


@pytest.mark.asyncio
async def test_homs_url_with_valid_homID():
    """Test for valid "homs" URL with a valid homID."""
    url = await _btdb2_url_factory("homs", homID="12345")
    assert url == "https://data.ninjakiwi.com/battles2/homs/12345/leaderboard"


@pytest.mark.asyncio
async def test_homs_url_with_invalid_homID():
    """Test for invalid "homs" URL with an invalid homID."""
    url = await _btdb2_url_factory("homs", homID="invalid!@#")
    assert url is None


@pytest.mark.asyncio
async def test_users_url_with_valid_userID():
    """Test for valid "users" URL with a valid userID."""
    url = await _btdb2_url_factory("users", userID="oak_cce22SUMHERE")
    assert url == "https://data.ninjakiwi.com/battles2/users/oak_cce22SUMHERE"


@pytest.mark.asyncio
async def test_users_url_with_invalid_userID():
    """Test for invalid "users" URL with an invalid userID."""
    url = await _btdb2_url_factory("users", userID="invalid!@#")
    assert url is None
