"""Main module."""

from typing import Callable

from .API import btd6_url_factory, btdb2_url_factory
from .FUNCTIONS import api_fetch, error_handler


async def _game_to_func(game: str, data: str) -> str | None:
    games = {
        "BTD6": btd6_url_factory,
        "BTDB2": btdb2_url_factory,
    }
    try:
        for entry, func in games.items():
            if game == entry:
                return await func(data)
    except (AttributeError, TypeError):
        await error_handler(act="str", exception=f"Game {game} not found.")
        return None


async def fetch(game: str, data: str) -> dict | None:
    url = await _game_to_func(game, data)
    if url is not None:
        return await api_fetch(url)
    else:
        return None
