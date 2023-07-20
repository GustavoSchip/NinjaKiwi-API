"""FUNCTION-level package for NinjaKiwi API."""

import json
from typing import Optional

import aiohttp


class _model:
    def __init__(self, data: dict, response: aiohttp.ClientResponse):
        self.response = response
        self.data = data

    async def get_raw_data(self) -> dict | None:
        return await self.response.json()

    async def get_data(self, **options) -> dict | None:
        atr = {}
        options_found = False

        for option_name, option_value in options.items():
            temp = self.data.get(option_name)
            if temp is not None:
                atr[option_name] = temp
                if not options_found:
                    options_found = True

        if not options_found:
            return None
        else:
            return atr


async def _handler(
    data: dict | None, response: aiohttp.ClientResponse | None
) -> Optional[_model] | None:
    if data is None or response is None:
        return None
    return _model(data, response)
