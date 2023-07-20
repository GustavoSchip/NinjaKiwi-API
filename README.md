
---

<div align="center">
  <h1>NinjaKiwi API</h1>
</div>

<p align="center">
<a href="https://pypi.python.org/pypi/ninjakiwi_api">
    <img src="https://img.shields.io/pypi/v/ninjakiwi-api.svg"
        alt = "Release Status">
</a>
</p>

<br>

This project was born because of the need of an API wrapper for the NinjaKiwi API. (A.K.A. Open Data)
<br>
Do note that this is my first ever library and I still have a lot to learn!
<br>
The games supported in [Open Data](https://data.ninjakiwi.com/) are:

- #### [Bloons Tower Defence 6](https://ninjakiwi.com/our-games#bloonstd6)

- #### [Bloons Tower Defence Battles 2](https://ninjakiwi.com/our-games#battles)

# Usage

To import the module use:
<br>

```python
import ninjakiwi_api
```

All the functions, models/classes and attributes are as followed:

### `fetch` Function

The [`fetch`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/main.py) function is used to asynchronously fetch data from the NinjaKiwi API based on the specified game and data type.

**Parameters:**

- `game` (str): The game for which data will be fetched. Valid options are "BTD6" and "BTDB2".
- `data` (str): The type of data to fetch. The supported data types depend on the specified game.
- `**options`: Additional options that can be passed to customize the data retrieval process.

**Returns:**

`Optional[_model] | None`: A Union containing the fetched data as an instance of the `_model` class if successful, or None if the data could not be fetched.

**Raises:**

- `Warning`: Any exceptions that might be raised during the data fetching process.

**Notes:**

- This function is an asynchronous function, and it uses the [`_game_to_func`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/main.py) function internally to generate the API URL.
- The [`_api_fetch`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/FUNCTIONS/FETCH/function.py) function is used to perform the actual HTTP request and fetch the data from the API.
- The returned dictionary will vary depending on the specific data being fetched.
- If the provided game or data is not recognized or supported, the function returns None.

**See also:**

- [`_game_to_func`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/main.py): Function used internally to generate the API URL based on the game and data type.
- [`_api_fetch`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/FUNCTIONS/FETCH/function.py): Function used to perform the actual HTTP request and fetch data from the API.
- [`_btd6_url_factory`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/API/BTD6/function.py): Function used to construct the API URL for Bloons TD 6.
- [`_btdb2_url_factory`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/API/BTDB2/function.py): Function used to construct the API URL for Bloons TD Battles 2.

**Examples:**

Fetch race data for BTD6:
<br>

```python
data = await fetch("BTD6", "races")
if data is not None:
    raw = await data.get_raw_data()
    example = await data.get_data("id")
    print(f"Successfully fetched race data: {raw}")
    if example is not None:
        print(f"Successfully fetched race data: {example}")
else:
    print("Failed to fetch race data.")
```

Fetch HOM leaderboard for BTDB2:
<br>

```python
data = await fetch("BTDB2", "homs")
if data is not None:
    leaderboard = await data.get_data("leaderboard")
    print(f"Successfully fetched HOM leaderboard: {leaderboard}")
else:
    print("Failed to fetch HOM leaderboard.")
```

### `_model` Class

The [`_model`](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/ninjakiwi_api/FUNCTIONS/FETCH/model.py) class represents a data model with methods to access and retrieve information from the data.

**Parameters:**

- `data` (dict): The decoded JSON data containing the information.
- `response` (aiohttp.ClientResponse): The HTTP response object.

**Attributes:**

- `response` (aiohttp.ClientResponse): The HTTP response object.
- `data` (dict): The decoded JSON data containing the information.

**Methods:**

- `async def get_raw_data(self) -> dict | None`: Get the raw JSON data from the HTTP response. Returns the raw JSON data as a Python dictionary, or None if there was an error retrieving the data.

- `async def get_data(self, name: str) -> List[Union[dict, list, str, int, float, bool, None]] | None`: Get the values corresponding to the given name from the data. Returns the values corresponding to the given name as a list. Returns None if no matching entries are found in the data or if all matching entries have a value of None.

**Examples:**

Fetch race data for BTD6 and get raw response:
<br>

```python
instance_of_model = await fetch("BTD6", "races")

raw_data = await instance_of_model.get_raw_data()
if raw_data is not None:
    print(f"Raw data: {raw_data}")
else:
    print("Failed to fetch raw data.")
```

Fetch race data for BTD6 and get specific type of data:
<br>

```python
instance_of_model = await fetch("BTD6", "races")

specific_data = await instance_of_model.get_data("id")
if specific_data is not None:
    print(f"Specific data: {specific_data}")
else:
    print("Failed to fetch specific data.")
```

# Example

In this example we make a request to the api and we want the value of `id`.
<br>

```python
import asyncio
from ninjakiwi_api import fetch


async def start():
    data = await fetch("BTD6", "races")
    if data is not None:
        raw = await data.get_raw_data()
        example = await data.get_data("id")
        print(f"Successfully fetched race data: {raw}")
        if example is not None:
            print(f"Successfully fetched race data: {example}")
    else:
        print("Failed to fetch race data.")


def main():
    asyncio.run(start())


if __name__ == "__main__":
    main()
```

## Additional info

[LICENSE](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/LICENSE)
<br>
[CONTRIBUTING](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/CONTRIBUTING.md)

---
