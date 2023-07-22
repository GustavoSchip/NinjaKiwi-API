
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

## installation

To get the latest release use:
<br>

```commandline
    $ python -m pip install --upgrade ninjakiwi-api
```

## Alternative installation

To get the latest release via a tarball use: <br>
To check which version the library is on go to [Releases](https://github.com/GustavoSchip/NinjaKiwi-API/releases) and search for releases!
<br>

```commandline
    $ python -m pip install --upgrade https://github.com/GustavoSchip/NinjaKiwi-API/releases/download/v{VERSION-NUMBER-HERE}/ninjakiwi_api-{VERSION-NUMBER-HERE}.tar.gz
```

To get the latest pre-release via a tarball use: <br>
To check which version the library (dev) is on go to [Releases](https://github.com/GustavoSchip/NinjaKiwi-API/releases) and search for pre-releases!
<br>

```commandline
    $ python -m pip install --upgrade --pre https://github.com/GustavoSchip/NinjaKiwi-API/releases/download/v{VERSION-NUMBER-HERE}-dev/ninjakiwi_api-{VERSION-NUMBER-HERE}.tar.gz
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

# Documentation

The documentation is available on the project its [Wiki](https://github.com/GustavoSchip/NinjaKiwi-API/wiki)!

## Additional info

[LICENSE](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/LICENSE)
<br>
[CONTRIBUTING](https://github.com/GustavoSchip/NinjaKiwi-API/blob/master/CONTRIBUTING.md)

---
