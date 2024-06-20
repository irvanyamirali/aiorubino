from typing import Optional

import aiorubino


class Users:

    def __init__(self: "aiorubino.Client"):
        pass

    async def get_my_profile_info(self, profile_id: Optional[str] = None) -> dict:
        """
        Get your page information.
        If you want to access your page information, you don't need to enter the profile_id parameter.
        """
        params: dict = {
            "profile_id": profile_id
        }
        return await self.api.execute(name="getMyProfileInfo", data=params)
