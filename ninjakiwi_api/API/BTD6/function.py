"""API-level package for NinjaKiwi API."""

import re
from enum import Enum
from typing import Optional

__endpoint__ = "https://data.ninjakiwi.com/"
__game__ = "btd6"


class ChallengeFilter(str, Enum):
    NEWEST = "newest"
    TRENDING = "trending"
    DAILY = "daily"


class BossEvent(str, Enum):
    STANDARD = "standard"
    ELITE = "elite"


class OdysseyDifficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


async def btd6_url_factory(data: str, **options) -> Optional[str]:
    types = [
        "races",
        "bosses",
        "challenges",
        "ct",
        "odyssey",
    ]

    if data not in types:
        return None

    base_url = f"{__endpoint__}{__game__}/{data}"

    if data == "races":
        return base_url

    if data == "bosses":
        bossID = options.get("bossID")
        if bossID is not None:
            bossID_pattern = re.compile(r"^[A-Za-z0-9_-]+$")
            if not bossID_pattern.match(bossID):
                return None

            type_ = options.get("type")
            teamSize = options.get("teamSize")
            if type_ not in BossEvent.__members__ or teamSize != "1":
                return None

            return f"{base_url}/{bossID}/leaderboard/{type_}/{teamSize}"
        else:
            return base_url

    if data == "challenges":
        challengeFilter = options.get("challengeFilter")
        if challengeFilter not in ChallengeFilter.__members__:
            return None

        return f"{base_url}/filter/{challengeFilter}"

    if data == "ct":
        ctID = options.get("ctID")
        if ctID is not None:
            return f"{base_url}/{ctID}/leaderboard/player"
        else:
            return base_url

    if data == "odyssey":
        odysseyID = options.get("odysseyID")
        difficulty = options.get("difficulty")
        if odysseyID is not None and difficulty in OdysseyDifficulty.__members__:
            maps = options.get("maps")
            if maps is not None:
                return f"{base_url}/{odysseyID}/{difficulty}/maps"
            else:
                return f"{base_url}/{odysseyID}/{difficulty}"
        else:
            return base_url

    if data == "users":
        userID = options.get("userID")
        userID_pattern = re.compile(r"^[A-Za-z0-9_-]+$")
        if userID is not None and userID_pattern.match(userID):
            return f"{base_url}/{userID}"
        else:
            return None

    if data == "guild":
        guildID = options.get("guildID")
        guildID_pattern = re.compile(r"^[A-Za-z0-9_-]+$")
        if guildID is not None and guildID_pattern.match(guildID):
            return f"{base_url}/{guildID}"
        else:
            return None

    if data == "save":
        oakID = options.get("oakID")
        oakID_pattern = re.compile(r"^[A-Za-z0-9_-]+$")
        if oakID is not None and oakID_pattern.match(oakID):
            return f"{base_url}/{oakID}"
        else:
            return None

    return None
