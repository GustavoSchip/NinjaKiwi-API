"""FUNCTION-level package for NinjaKiwi API."""

import json
from typing import Optional, Union

import aiohttp


class _model:
    """
    Represents a data model with methods to access and retrieve information from the data.

    Parameters
    ----------
    data : dict
        The decoded JSON data containing the information.
    response : aiohttp.ClientResponse
        The HTTP response object.

    Attributes
    ----------
    response : aiohttp.ClientResponse
        The HTTP response object.
    data : dict
        The decoded JSON data containing the information.
    """
    def __init__(self, data: dict, response: aiohttp.ClientResponse):
        self.response = response
        self.data = data

    async def get_raw_data(self) -> dict | None:
        """
        Get the raw JSON data from the HTTP response.

        Returns
        -------
        dict | None
            The raw JSON data as a Python dictionary, or None if there was an error
            retrieving the data.
        """
        return await self.response.json()

    async def get_data(self, name: str) -> Union[dict, list, str, int, float, bool, None] | None:
        """
        Get the value corresponding to the given name from the data.

        Parameters
        ----------
        name : str
            The name of the entry to retrieve.

        Returns
        -------
        Union[dict, list, str, int, float, bool, None] | None
            The value corresponding to the given name, or None if the name
            was not found in the data.
        """
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
