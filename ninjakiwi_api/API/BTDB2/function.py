"""API-level package for NinjaKiwi API."""

from enum import Enum
from typing import Optional

__endpoint__ = "https://data.ninjakiwi.com/"
__game__ = "battles2"


class _ChallengeFilter(str, Enum):
    NEWEST = "newest"
    TRENDING = "trending"
    DAILY = "daily"


async def _btdb2_url_factory(data: str, **options) -> Optional[str]:
    """
    Construct the NinjaKiwi API URL for Bloons TD Battles 2 based on the specified data and options.

    Parameters
    ----------
    data : str
        The type of data to fetch. The supported data types are:
        "homs" and "users".

    **options : Any
        Additional options to customize the API URL based on the data type.

    Returns
    -------
    Optional[str]
        The constructed API URL as a string if the data and options are valid, otherwise None.

    Notes
    -----
    - This function generates the API URL for various Bloons TD Battles 2 data types based on the input parameters.
    - The constructed URL is specific to the NinjaKiwi API for Bloons TD Battles 2.

    Parameters for each data type:
    ------------------------------
    homs:
        homID : str
            The ID of the Hall of Masters event for which the leaderboard is fetched.

    users:
        userID : str
            The ID of the player for which the data is fetched.
    """

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
            if all(c.isalnum() or c in "_-" for c in homID):
                return f"{base_url}/{homID}/leaderboard"
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

    return None
