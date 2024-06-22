from aiorubino.types import Results

import aiorubino

from typing import Optional


class Users:

    def __init__(self: "aiorubino.Client"):
        pass

    async def get_my_profile_info(self, profile_id: Optional[str] = None) -> Results:
        """
        Get your page information.
        If you want to access your page information, you don't need to enter the profile_id parameter.
        """
        params: dict = {
            "profile_id": profile_id
        }
        return await self.api.execute(name="getMyProfileInfo", data=params)
