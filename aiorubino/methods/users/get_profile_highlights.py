from typing import Optional

from aiorubino.types import Results
import aiorubino


class GetProfileHighlights:

    async def get_profile_highlights(
            self: "aiorubino.Client",
            target_profile_id: str,
            profile_id: Optional[str] = None
    ) -> Results:
        """
        Get profile highlights
        """
        params: dict = {
            "target_profile_id": target_profile_id,
            "profile_id": profile_id
        }
        return await self.api.execute(name="getProfileHighlights", data=params)
