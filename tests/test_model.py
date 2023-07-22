#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest
from aiohttp import test_utils

from ninjakiwi_api.FUNCTIONS.FETCH.model import model, btd6_model, btdb2_model


@pytest.mark.asyncio
async def test_get_raw_data():
    """Test for get_raw_data"""
    data = {
        "name": "Test User",
        "score": 100,
        "info": {"level": 10, "status": "active"},
    }

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=data)
    request.status = 200

    my_model = model(data, request)

    raw_data = await my_model.get_raw_data()
    assert raw_data == data


@pytest.mark.asyncio
async def test_get_data():
    """Test for get_data"""
    data = {
        "name": ["Ninja", "Monkey", "Banana"],
        "score": [100, 200, 50],
        "info": {"level": 10, "status": "active"},
    }

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=data)
    request.status = 200

    my_model = model(data, request)

    names = await my_model.get_data("name")
    assert names == [["Ninja", "Monkey", "Banana"]]

    scores = await my_model.get_data("score")
    assert scores == [[100, 200, 50]]

    level = await my_model.get_data("info")
    assert level == [{"level": 10, "status": "active"}]

    invalid_name = await my_model.get_data("invalid_name")
    assert invalid_name is None


@pytest.mark.asyncio
async def test_get_homid():
    """Test for get_homid"""
    data = {
        "id": "lj44j3vt",
        "name": "Season 13",
        "start": 1687428000000,
        "end": 1692180000000,
        "totalScores": 254,
        "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_12/leaderboard",
    }

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=data)
    request.status = 200

    my_model = btdb2_model(data, request)

    homid_1 = await my_model.get_homid(0)
    assert homid_1 == "season_13"

    homid_2 = await my_model.get_homid(1)
    assert homid_2 is None


@pytest.mark.asyncio
async def test_get_next_season():
    """Test for get_next_season"""
    data = {
        "id": "lj44j3vt",
        "name": "Season 13",
        "start": 1687428000000,
        "end": 1692180000000,
        "totalScores": 254,
        "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_12/leaderboard",
    }

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=data)
    request.status = 200

    my_model = btdb2_model(data, request)

    future_season = await my_model.get_next_season()
    assert future_season == "season_13"


@pytest.mark.asyncio
async def test_get_current_season():
    """Test for get_current_season"""
    data = [
        {
            "id": "lj44j3vt",
            "name": "Season 13",
            "start": 1687428000000,
            "end": 1692180000000,
            "totalScores": 254,
            "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_12/leaderboard",
        },
        {
            "id": "41546",
            "name": "Season 12",
            "start": 1687428000000,
            "end": 1692180000000,
            "totalScores": 254,
            "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_11/leaderboard",
        },
    ]

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=data)
    request.status = 200

    my_model = btdb2_model(data, request)

    future_season = await my_model.get_current_season()
    assert future_season == "season_12"


@pytest.mark.asyncio
async def test_get_previous_season():
    """Test for get_previous_season"""
    data = [
        {
            "id": "lj44j3vt",
            "name": "Season 13",
            "start": 1687428000000,
            "end": 1692180000000,
            "totalScores": 254,
            "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_12/leaderboard",
        },
        {
            "id": "54321",
            "name": "Season 12",
            "start": 0,
            "end": 0,
            "totalScores": 254,
            "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_11/leaderboard",
        },
        {
            "id": "12345",
            "name": "Season 11",
            "start": 0,
            "end": 0,
            "totalScores": 254,
            "leaderboard": "https://data.ninjakiwi.com/battles2/homs/season_10/leaderboard",
        },
    ]

    request = test_utils.make_mocked_request("GET", "/test")
    request.json = test_utils.make_mocked_coro(return_value=data)
    request.status = 200

    my_model = btdb2_model(data, request)

    future_season = await my_model.get_previous_season()
    assert future_season == "season_11"
