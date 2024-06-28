from typing import Optional

from aiorubino.types import Results
import aiorubino


class GetRecentFollowingPosts:

    async def get_recent_following_posts(
            self: "aiorubino.Client",
            profile_id: Optional[str] = None,
            limit: Optional[int] = 20,
            sort: Optional[str] = "FromMax",
            max_id: Optional[str] = None
    ) -> Results:
        """
        Get recent following posts
        """
        params: dict = {
            "profile_id": profile_id,
            "limit": limit,
            "sort": sort,
            "max_id": max_id
        }
        return await self.api.execute(name="getRecentFollowingPosts", data=params)
