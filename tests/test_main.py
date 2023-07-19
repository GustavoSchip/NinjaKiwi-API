#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest


@pytest.mark.asyncio
async def test_fetch():
    """Sample pytest test function."""
    from ninjakiwi_api import fetch

    results = await fetch("BTD6", "races")

    assert "success" in results
