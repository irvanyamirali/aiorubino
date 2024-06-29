from typing import Optional

from aiorubino.types import Results
import aiorubino


class GetMyProfileInfo:

    async def get_my_profile_info(self: "aiorubino.Client", profile_id: Optional[str] = None) -> Results:
        """
        Get your page information.
        If you want to access your page information, you don't need to enter the profile_id parameter.
        """
        params: dict = {
            "profile_id": profile_id
        }
        return await self.api.execute(name="getMyProfileInfo", data=params)
