"""FUNCTION-level package for NinjaKiwi API."""

from aiohttp import ClientResponse


async def _error_handler(
    act: str, response: ClientResponse = None, exception: str = None
) -> None:

    err = None

    if act == "http":
        if response is not None:
            try:
                data = await response.json()
            except AttributeError:
                data = None
            try:
                status = response.status
            except (KeyError, AttributeError):
                status = None

            if status is not None:
                if data is None:
                    raise Exception("No valid data!")
                if status == 200:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                elif status == 404:
                    try:
                        err = await response.read()
                    except KeyError:
                        err = status
                elif status == 500:
                    try:
                        err = await response.read()
                    except KeyError:
                        err = status
                else:
                    raise Exception("Not a valid HTTP status!")
            else:
                raise Exception("Not a valid HTTP response!")
        else:
            raise Exception("Not a valid HTTP response!")

    elif act == "str":
        if exception is not None and isinstance(exception, str):
            err = exception
        else:
            raise Exception("Not a valid exception!")

    else:
        raise Exception("Not a valid action!")

    if err is not None:
        raise Warning(err)

    return None
