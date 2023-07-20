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

# Usage

...

# Example

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
