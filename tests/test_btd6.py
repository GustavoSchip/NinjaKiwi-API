#!/usr/bin/env python
"""Tests for `ninjakiwi_api` package."""
# pylint: disable=redefined-outer-name

import pytest

from ninjakiwi_api.API import _btd6_url_factory


@pytest.mark.asyncio
async def test_valid_races_url():
    """Test for valid races URL."""
    races_url = await _btd6_url_factory("races")
    assert races_url == "https://data.ninjakiwi.com/btd6/races"


@pytest.mark.asyncio
async def test_valid_bosses_url():
    """Test for valid bosses URL."""
    bosses_url = await _btd6_url_factory(
        "bosses", bossID="some_boss_id", type="standard", teamSize="1"
    )
    assert (
        bosses_url
        == "https://data.ninjakiwi.com/btd6/bosses/some_boss_id/leaderboard/standard/1"
    )


@pytest.mark.asyncio
async def test_invalid_bosses_url_invalid_bossID():
    """Test for invalid bosses URL due to invalid bossID."""
    invalid_bosses_url = await _btd6_url_factory(
        "bosses", bossID="!@#invalid_boss_id", type="standard", teamSize="1"
    )
    assert invalid_bosses_url is None


@pytest.mark.asyncio
async def test_invalid_bosses_url_invalid_type():
    """Test for invalid bosses URL due to invalid type."""
    invalid_bosses_url = await _btd6_url_factory(
        "bosses", bossID="some_boss_id", type="invalid_type", teamSize="1"
    )
    assert invalid_bosses_url is None


@pytest.mark.asyncio
async def test_valid_challenges_url():
    """Test for valid challenges URL with filter."""
    challenges_url = await _btd6_url_factory("challenges", challengeFilter="newest")
    assert challenges_url == "https://data.ninjakiwi.com/btd6/challenges/filter/newest"


@pytest.mark.asyncio
async def test_invalid_challenges_url_invalid_filter():
    """Test for invalid challenges URL due to invalid filter."""
    invalid_challenges_url = await _btd6_url_factory(
        "challenges", challengeFilter="invalid_filter"
    )
    assert invalid_challenges_url is None


@pytest.mark.asyncio
async def test_valid_ct_url():
    """Test for valid ct URL with ctID."""
    ct_url = await _btd6_url_factory("ct", ctID="some_ct_id")
    assert ct_url == "https://data.ninjakiwi.com/btd6/ct/some_ct_id/leaderboard/player"


@pytest.mark.asyncio
async def test_invalid_ct_url():
    """Test for invalid ct URL due to missing ctID."""
    invalid_ct_url = await _btd6_url_factory("ct")
    assert invalid_ct_url == "https://data.ninjakiwi.com/btd6/ct"


@pytest.mark.asyncio
async def test_valid_odyssey_url():
    """Test for valid odyssey URL with odysseyID and difficulty."""
    odyssey_url = await _btd6_url_factory(
        "odyssey", odysseyID="some_odyssey_id", difficulty="hard"
    )
    assert odyssey_url == "https://data.ninjakiwi.com/btd6/odyssey/some_odyssey_id/hard"


@pytest.mark.asyncio
async def test_invalid_odyssey_url_missing_odysseyID():
    """Test for invalid odyssey URL due to missing odysseyID."""
    invalid_odyssey_url = await _btd6_url_factory("odyssey", difficulty="hard")
    assert invalid_odyssey_url == "https://data.ninjakiwi.com/btd6/odyssey"


@pytest.mark.asyncio
async def test_invalid_odyssey_url_invalid_difficulty():
    """Test for invalid odyssey URL due to invalid difficulty."""
    invalid_odyssey_url = await _btd6_url_factory(
        "odyssey", odysseyID="some_odyssey_id", difficulty="invalid_difficulty"
    )
    assert invalid_odyssey_url is None


@pytest.mark.asyncio
async def test_valid_odyssey_url_with_maps():
    """Test for valid odyssey URL with odysseyID, difficulty, and maps."""
    odyssey_url_with_maps = await _btd6_url_factory(
        "odyssey",
        odysseyID="some_odyssey_id",
        difficulty="medium",
        maps=["map1", "map2"],
    )
    assert (
        odyssey_url_with_maps
        == "https://data.ninjakiwi.com/btd6/odyssey/some_odyssey_id/medium/maps"
    )


@pytest.mark.asyncio
async def test_valid_users_url():
    """Test for valid users URL with userID."""
    users_url = await _btd6_url_factory("users", userID="oak_cce22SUMHERE")
    assert users_url == "https://data.ninjakiwi.com/btd6/users/oak_cce22SUMHERE"


@pytest.mark.asyncio
async def test_invalid_users_url_invalid_userID():
    """Test for invalid users URL due to invalid userID."""
    invalid_users_url = await _btd6_url_factory("users", userID="!@#invalid_user_id")
    assert invalid_users_url is None


@pytest.mark.asyncio
async def test_valid_guild_url():
    """Test for valid guild URL with guildID."""
    guild_url = await _btd6_url_factory("guild", guildID="some_guild_id")
    assert guild_url == "https://data.ninjakiwi.com/btd6/guild/some_guild_id"


@pytest.mark.asyncio
async def test_invalid_guild_url_invalid_guildID():
    """Test for invalid guild URL due to invalid guildID."""
    invalid_guild_url = await _btd6_url_factory("guild", guildID="!@#invalid_guild_id")
    assert invalid_guild_url is None


@pytest.mark.asyncio
async def test_valid_save_url():
    """Test for valid save URL with oakID."""
    save_url = await _btd6_url_factory("save", oakID="some_oak_id")
    assert save_url == "https://data.ninjakiwi.com/btd6/save/some_oak_id"


@pytest.mark.asyncio
async def test_invalid_save_url_invalid_oakID():
    """Test for invalid save URL due to invalid oakID."""
    invalid_save_url = await _btd6_url_factory("save", oakID="!@#invalid_oak_id")
    assert invalid_save_url is None


@pytest.mark.asyncio
async def test_invalid_data_type():
    invalid_data_url = await _btd6_url_factory("invalid_data_type")
    assert invalid_data_url is None
