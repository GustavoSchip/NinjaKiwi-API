"""API-level package for NinjaKiwi API."""

import re
from enum import Enum
from typing import Optional

__endpoint__ = "https://data.ninjakiwi.com/"
__game__ = "battles2"


class _ChallengeFilter(str, Enum):
    NEWEST = "newest"
    TRENDING = "trending"
    DAILY = "daily"


async def _btdb2_url_factory(data: str, **options) -> Optional[str]:
    types = [
        "homs",
        "users",
    ]

    if data not in types:
        return None

    base_url = f"{__endpoint__}{__game__}/{data}"

    if data == "homs":
        homID = options.get("homID")
        if homID is not None:
            homID_pattern = re.compile(r"^[A-Za-z0-9_-]+$")
            if not homID_pattern.match(homID):
                return None
            return f"{base_url}/{homID}/leaderboard"
        else:
            return base_url

    if data == "users":
        userID = options.get("userID")
        userID_pattern = re.compile(r"^[A-Za-z0-9_-]+$")
        if userID is not None and userID_pattern.match(userID):
            return f"{base_url}/{userID}"

        return None

    return None
