from aiorubino.types import Results

from typing import Optional
from random import randint

import aiohttp


class API:

    BASE_URL = f"https://rubino{randint(1, 19)}.iranlms.ir"

    HEADERS: dict = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "okhttp/3.12.1",
    }

    def __init__(self, client=None):
        """
        Initialize the API instance.

        :param client: The client instance which contains auth and other configurations.
        """
        self.client = client

    async def execute(self, name: str, data: Optional[dict] = None, method: Optional[str] = "POST"):
        """
        Execute a command on the Rubino API
        """
        payload = {
            "auth": self.client.auth,
            "api_version": "0",
            "client": {
                "app_name": "Main",
                "app_version": "3.0.9",
                "lang_code": "en",
                "package": "app.rbmain.a",
                "platform": "Android",
                "temp_code": "10"
            },
            "data": data,
            "method": name
        }
        for _ in range(self.client.max_retry):
            async with aiohttp.ClientSession(base_url=self.BASE_URL) as session:
                async with session.request(method=method, url="/", json=payload) as res:
                    response_data = await res.json()
                    if response_data.get("status") == "OK":
                        response_data.pop("status")
                        return Results(response_data)
                    error_code = response_data.get("status_det")
                    description = response_data.get("description")
                    raise Exception(error_code, description)
