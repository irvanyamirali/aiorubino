from typing import Optional

from aiorubino.types import Results
import aiorubino


class UnFollow:

    async def un_follow(
            self: "aiorubino.Client",
            followee_id: str,
            f_type: Optional[str] = "UnFollow",
            profile_id: Optional[str] = None
    ) -> Results:
        params: dict = {
            "followee_id": followee_id,
            "f_type": f_type,
            "profile_id": profile_id
        }
        return await self.api.execute(name="requestFollow", data=params)
