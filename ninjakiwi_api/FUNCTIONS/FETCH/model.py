"""FUNCTION-level package for NinjaKiwi API."""

import json
from typing import Optional, Union, List

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

    async def get_data(
        self, name: str
    ) -> List[Union[dict, list, str, int, float, bool, None]] | None:
        """
        Get the values corresponding to the given name from the data.

        Parameters
        ----------
        name : str
            The name of the entries to retrieve.

        Returns
        -------
        List[Union[dict, list, str, int, float, bool]] | None
            The values corresponding to the given name. Returns None if no matching entries
            are found in the data or if all matching entries have a value of None.
        """
        result = []
        found_entries = False

        for entry in self.data.get("body", []):
            for key, value in entry.items():
                if key == name:
                    if not found_entries:
                        found_entries = True
                    if value is not None:
                        result.append(value)

        if not found_entries:
            return None

        return result if result else None


async def _handler(
    data: dict | None, response: aiohttp.ClientResponse | None
) -> Optional[_model] | None:
    if data is None or response is None:
        return None
    return _model(data, response)
