from typing import Optional

import aiorubino
from aiorubino.types import Results


class Users:

    async def get_my_profile_info(self: "aiorubino.Client", profile_id: Optional[str] = None) -> Results:
        """
        Get your page information.
        If you want to access your page information, you don't need to enter the profile_id parameter.
        """
        params: dict = {
            "profile_id": profile_id
        }
        return await self.api.execute(name="getMyProfileInfo", data=params)

    async def get_profile_highlights(
            self: "aiorubino.Client",
            target_profile_id: str,
            profile_id: Optional[str] = None
    ) -> Results:
        params: dict = {
            "target_profile_id": target_profile_id,
            "profile_id": profile_id
        }
        return await self.api.execute(name="getProfileHighlights", data=params)

    async def follow(
            self: "aiorubino.Client",
            followee_id: str, f_type: Optional[str] = "Follow",
            profile_id: Optional[str] = None
    ) -> Results:
        params: dict = {
            "followee_id": followee_id,
            "f_type": f_type,
            "profile_id": profile_id
        }
        return await self.api.execute(name="requestFollow", data=params)

    async def get_recent_following_posts(
            self: "aiorubino.Client",
            profile_id: Optional[str] = None,
            limit: Optional[int] = 20,
            sort: Optional[str] = "FromMax",
            max_id: Optional[str] = None
    ) -> Results:
        params: dict = {
            "profile_id": profile_id,
            "limit": limit,
            "sort": sort,
            "max_id": max_id
        }
        return await self.api.execute(name="getRecentFollowingPosts", data=params)
