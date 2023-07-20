"""FUNCTION-level package for NinjaKiwi API."""

import json
from typing import Optional, Union

import aiohttp


class _model:
    def __init__(self, data: dict, response: aiohttp.ClientResponse):
        self.response = response
        self.data = data

    async def get_raw_data(self) -> dict | None:
        return await self.response.json()

    async def get_data(self, name: str) -> Union[dict, list, str, int, float, bool, None] | None:
        for entry in self.data.get("body", []):
            if entry:
                for key, value in entry.items():
                    if key == name:
                        return value
        return None


async def _handler(
    data: dict | None, response: aiohttp.ClientResponse | None
) -> Optional[_model] | None:
    if data is None or response is None:
        return None
    return _model(data, response)
