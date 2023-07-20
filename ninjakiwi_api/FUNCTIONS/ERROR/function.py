"""FUNCTION-level package for NinjaKiwi API."""

from aiohttp import ClientResponse


async def _error_handler(
    act: str, response: ClientResponse = None, exception: str = None
) -> None:

    err = None

    if act == "http":
        if response is not None:
            data = await response.json()
            status = response.status

            if status != 200:
                if status == 401:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                if status == 403:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                if status == 404:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                if status == 413:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                if status == 500:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                if status == 503:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status
                if status == 504:
                    try:
                        err = str(data["error"])
                    except KeyError:
                        err = status

        else:
            raise Exception

    elif act == "str":
        err = exception

    if err is not None:
        raise Warning(err)

    return None
