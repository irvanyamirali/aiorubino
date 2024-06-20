from typing import Optional

from aiorubino.api import API
from aiorubino.methods import Methods


class Client(Methods):

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
