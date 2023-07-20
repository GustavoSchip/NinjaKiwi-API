<div align="center">
  <h1>NinjaKiwi API</h1>
</div>

---

<p align="center">
<a href="https://pypi.python.org/pypi/ninjakiwi_api">
    <img src="https://img.shields.io/pypi/v/ninjakiwi-api.svg"
        alt = "Release Status">
</a>
</p>

<br>

This project was born because of the need of an API wrapper for the NinjaKiwi API. (A.K.A. OpenDATA)
<br>
Do note that this is my first ever library and I still have a lot to learn!

# Usage

To import the module use:
<br>

```python
import ninjakiwi_api
```

All the functions, models/classes and attributes are as followed:

```python
"""
TODO
"""
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

# Coming soon...

Stay tuned guys

---
