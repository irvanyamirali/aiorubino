from .get_my_profile_info import GetMyProfileInfo
from .get_profile_highlights import GetProfileHighlights
from .follow import Follow
from .unfollow import UnFollow
from .get_recent_following_posts import GetRecentFollowingPosts


class Users(GetMyProfileInfo, GetProfileHighlights, Follow, UnFollow, GetRecentFollowingPosts):
    pass
