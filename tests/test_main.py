#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest


@pytest.mark.asyncio
async def test_fetch_btd6():
    """Sample pytest test function."""
    from ninjakiwi_api import fetch

    results = await fetch("BTD6", "races")

    assert results is not None

    data = await results.get_raw_data()

    assert "success" in data


@pytest.mark.asyncio
async def test_fetch_btdb2():
    """Sample pytest test function."""
    from ninjakiwi_api import fetch

    results = await fetch("BTDB2", "homs")

    assert results is not None

    data = await results.get_raw_data()

    assert "success" in data
