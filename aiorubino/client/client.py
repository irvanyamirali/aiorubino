from aiorubino.api import API

from typing import Optional


class Client:

    def __init__(self, auth: str, max_retry: Optional[int] = 3):
        """
        Initialize the Client instance.
        :param auth: The auth of the account.
        """
        self.auth = auth
        self.max_retry = max_retry
        self.api = API(client=self)

        if not isinstance(auth, str):
            raise ValueError("`auth` is `string` arg.")
