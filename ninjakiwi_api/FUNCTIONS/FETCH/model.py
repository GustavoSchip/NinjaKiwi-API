"""FUNCTION-level package for NinjaKiwi API."""

import json
from typing import List, Optional, Union

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

        def traverse(data, target_name):
            results = []
            if isinstance(data, dict):
                for key, value in data.items():
                    if key == target_name:
                        if value is not None:
                            results.append(value)
                    elif isinstance(value, (dict, list)):
                        results.extend(traverse(value, target_name))
            elif isinstance(data, list):
                for item in data:
                    results.extend(traverse(item, target_name))
            return results

        results = traverse(self.data, name)
        return results if results else None


async def _handler(
    data: dict | None, response: aiohttp.ClientResponse | None
) -> Optional[_model] | None:
    if data is None or response is None:
        return None
    return _model(data, response)
