from typing import Optional

from aiorubino.types import Results
import aiorubino


class Follow:

    async def follow(
            self: "aiorubino.Client",
            followee_id: str,
            f_type: Optional[str] = "Follow",
            profile_id: Optional[str] = None
    ) -> Results:
        params: dict = {
            "followee_id": followee_id,
            "f_type": f_type,
            "profile_id": profile_id
        }
        return await self.api.execute(name="requestFollow", data=params)
