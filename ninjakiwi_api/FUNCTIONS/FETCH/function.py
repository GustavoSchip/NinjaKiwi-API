"""FUNCTION-level package for NinjaKiwi API."""

from typing import Optional

import aiohttp

from ninjakiwi_api.FUNCTIONS.ERROR import _error_handler
from ninjakiwi_api.FUNCTIONS.FETCH.model import _handler, _model


async def _api_fetch(url: str) -> Optional[_model] | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                try:
                    return await _handler(data, response)
                except Exception:
                    return await _error_handler(act="http", response=response)
            else:
                return await _error_handler(act="http", response=response)
