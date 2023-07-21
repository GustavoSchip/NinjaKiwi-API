"""API-level package for NinjaKiwi API."""

from enum import Enum
from typing import Optional

__endpoint__ = "https://data.ninjakiwi.com/"
__game__ = "btd6"


class _ChallengeFilter(str, Enum):
    NEWEST = "newest"
    TRENDING = "trending"
    DAILY = "daily"


class _BossEvent(str, Enum):
    STANDARD = "standard"
    ELITE = "elite"


class _OdysseyDifficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


async def _btd6_url_factory(data: str, **options) -> Optional[str]:
    """
    Construct the NinjaKiwi API URL for Bloons TD 6 based on the specified data and options.

    Parameters
    ----------
    data : str
        The type of data to fetch. The supported data types are:
        "races", "bosses", "challenges", "ct", "odyssey", "users", "guild", and "save".

    **options : Any
        Additional options to customize the API URL based on the data type.

    Returns
    -------
    Optional[str]
        The constructed API URL as a string if the data and options are valid, otherwise None.

    Notes
    -----
    - This function generates the API URL for various Bloons TD 6 data types based on the input parameters.
    - The constructed URL is specific to the NinjaKiwi API for Bloons TD 6.

    Parameters for each data type:
    ------------------------------
    races:
        No additional options required.

    bosses:
        bossID : str
            The ID of the boss for which the leaderboard is fetched.

        type : str
            The type of leaderboard to fetch (e.g., "type1", "type2", etc.).

        teamSize : str
            The size of the team for the leaderboard (e.g., "1", "2", etc.).

    challenges:
        challengeFilter : str
            The filter to apply when fetching challenge data (e.g., "filter1", "filter2", etc.).

    ct:
        ctID : str
            The ID of the Collection Event for which the leaderboard is fetched.

    odyssey:
        odysseyID : str
            The ID of the Odyssey event for which the data is fetched.

        difficulty : str
            The difficulty level of the Odyssey (e.g., "easy", "medium", "hard").

        maps : list[str]
            Optional list of map names for the specified Odyssey event.

    users:
        userID : str
            The ID of the player for which the data is fetched.

    guild:
        guildID : str
            The ID of the guild for which the data is fetched.

    save:
        oakID : str
            The ID of the player's save data to fetch.
    """

    types = [
        "races",
        "bosses",
        "challenges",
        "ct",
        "odyssey",
        "users",
        "guild",
        "save",
    ]

    if data not in types:
        return None

    base_url = f"{__endpoint__}{__game__}/{data}"

    if data == "races":
        return base_url

    if data == "bosses":
        bossID = options.get("bossID")
        if bossID is not None:
            if all(c.isalnum() or c in "_-" for c in bossID):
                type_ = options.get("type")
                teamSize = options.get("teamSize")
                if type_ is not None:
                    type_ = type_.upper()
                    if type_ not in _BossEvent.__members__:
                        return None
                    elif teamSize is None:
                        teamSize = 1
                    else:
                        teamSize = int(
                            teamSize
                        )  # TODO : Warn about unsupported teamsize size!

                    type_ = type_.lower()

                    return f"{base_url}/{bossID}/leaderboard/{type_}/{teamSize}"
                else:
                    return None
            else:
                return None
        else:
            return base_url

    if data == "challenges":
        challengeFilter = options.get("challengeFilter")
        if challengeFilter is not None:
            challengeFilter = challengeFilter.upper()
            if challengeFilter in _ChallengeFilter.__members__:
                challengeFilter = challengeFilter.lower()
                return f"{base_url}/filter/{challengeFilter}"
            else:
                return None

        return base_url

    if data == "ct":
        ctID = options.get("ctID")
        if ctID is not None:
            if all(c.isalnum() or c in "_-" for c in ctID):
                return f"{base_url}/{ctID}/leaderboard/player"
            else:
                return None
        else:
            return base_url

    if data == "odyssey":
        odysseyID = options.get("odysseyID")
        difficulty = options.get("difficulty")
        if odysseyID is not None:
            difficulty = difficulty.upper()
            if difficulty is not None:
                if difficulty in _OdysseyDifficulty.__members__:
                    difficulty = difficulty.lower()
                    maps = options.get("maps")
                    if maps is not None:
                        return f"{base_url}/{odysseyID}/{difficulty}/maps"
                    else:
                        return f"{base_url}/{odysseyID}/{difficulty}"
                else:
                    return None
            else:
                return None
        else:
            return base_url

    if data == "users":
        userID = options.get("userID")
        if userID is not None:
            if all(c.isalnum() or c in "_-" for c in userID):
                return f"{base_url}/{userID}"
            else:
                return None
        else:
            return None

    if data == "guild":
        guildID = options.get("guildID")
        if guildID is not None:
            if all(c.isalnum() or c in "_-" for c in guildID):
                return f"{base_url}/{guildID}"
            else:
                return None
        else:
            return None

    if data == "save":
        oakID = options.get("oakID")
        if oakID is not None:
            if all(c.isalnum() or c in "_-" for c in oakID):
                return f"{base_url}/{oakID}"
            else:
                return None
        else:
            return None

    return None
