"""FUNCTION-level package for NinjaKiwi API."""

import json

import aiohttp

from ninjakiwi_api.FUNCTIONS.ERROR import _error_handler


async def _api_fetch(url: str) -> dict | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return await _error_handler(act="http", response=response)
