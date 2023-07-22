"""Main module."""

from typing import Optional

from ninjakiwi_api.FUNCTIONS.FETCH.model import model

from .API import _btd6_url_factory, _btdb2_url_factory
from .FUNCTIONS import _api_fetch, _error_handler


async def _game_to_func(game: str, data: str, **options) -> str | None:
    games = {
        "BTD6": _btd6_url_factory,
        "BTDB2": _btdb2_url_factory,
    }
    try:
        for entry, func in games.items():
            if game == entry:
                return await func(data, **options)
    except (AttributeError, TypeError):
        await _error_handler(act="str", exception=f"Game {game} not found.")
        return None


async def fetch(game: str, data: str, **options) -> Optional[model] | None:
    """
    Asynchronously fetches data from the NinjaKiwi API based on the specified game and data type.

    Parameters
    ----------
    game : str
        The game for which data will be fetched. Valid options are "btd6" and "btdb2".

    data : str
        The type of data to fetch. The supported data types depend on the specified game.

        For "BTD6" (Bloons TD 6):
            - "races": Returns information about races.
            - "bosses": Returns information about bosses and their leaderboards.
            - "challenges": Returns information about challenges.
            - "ct": Returns information about Collection Events and their leaderboards.
            - "odyssey": Returns information about Odyssey events and their maps.

        For "BTDB2" (Bloons TD Battles 2):
            - "homs": Returns a list of current Hall of Masters events or recent Hall of Masters positions for a player.
            - "leaderboard": Returns a HOM leaderboard for a specific event.
            - "users": Returns information about a Battles 2 Player.
            - "matches": Returns recent match information for a player.

    Returns
    -------
    Optional[model] | None
        A Union containing the fetched data if successful, or None if the data could not be fetched.

    Raises
    ------
    Warning
        Any exceptions that might be raised during the data fetching process.

    Notes
    -----
    - This function is an asynchronous function, and it uses the `_game_to_func` function internally to generate the API URL.
    - The `api_fetch` function is used to perform the actual HTTP request and fetch the data from the API.
    - The returned dictionary will vary depending on the specific data being fetched.
    - If the provided game or data is not recognized or supported, the function returns None.

    See also
    --------
    _game_to_func : Function used internally to generate the API URL based on the game and data type.
    _api_fetch : Function used to perform the actual HTTP request and fetch data from the API.
    _btd6_url_factory : Function used to construct the API URL for Bloons TD 6.
    _btdb2_url_factory : Function used to construct the API URL for Bloons TD Battles 2.

    Examples
    --------
    Fetch race data for BTD6:

        data = await fetch("BTD6", "races")
        if data is not None:
            raw = await data.get_raw_data()
            example = await data.get_data("id")
            print(f"Successfully fetched race data: {raw}")
            if example is not None:
                print(f"Successfully fetched race data: {example}")
        else:
            print("Failed to fetch race data.")

    Fetch HOM leaderboard for BTDB2:

        data = await fetch("BTDB2", "leaderboard")
        if data is not None:
            leaderboard = await data.get_data("leaderboard")
            print(f"Successfully fetched HOM leaderboard: {leaderboard}")
        else:
            print("Failed to fetch HOM leaderboard.")
    """

    url = await _game_to_func(game, data, **options)
    if url is not None:
        return await _api_fetch(url, game)
    else:
        return None
