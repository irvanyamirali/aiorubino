'''`Myrino` is an api-based library for Rubino messengers'''

from requests import session
from os.path import getsize
from random import randint

class Client:

    def __init__(
            self,
            auth: str = 'rnd',
            timeout: float = 20,
            platform: str = 'PWA',
            lang_code: str = 'en'
    ) -> None:
        self.auth : str = auth
        self.timeout: float = timeout
        self.session: function = session()
        self.client: dict = {
            'app_name': 'Main',
            'app_version': '3.0.1',
            'package': 'app.rubino.main',
            'lang_code': lang_code,
            'platform': platform
        }

        if auth.lower() == 'rnd':
            from .faker import rnd
            self.auth = rnd()

        if not self.auth:
            raise ValueError('`auth` did\'t passed')

    def __enter__(self) -> None:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.session.close()

    @property
    def url(self) -> str:
        return f'https://rubino{randint(1, 20)}.iranlms.ir/'

    async def exequte(self, method: str, data: dict, r_method: str = 'post') -> dict:
        payload: dict = {
            'api_version': '0',
            'auth': self.auth,
            'client': self.client,
            'data': data,
            'method': method
        }
        with self.session.request(method=r_method, url=self.url, timeout=self.timeout, json=payload) as r:
            return r.json()


    async def get_my_profile_info(self, profile_id: int = None) -> dict:
        '''!NOTE
        If the value of the `profile_id` parameter is selected as `None`,
        Robino servers will automatically select the default or main page.'''
        payload: dict = {
            'profile_id': profile_id
        }
        return await self.exequte('getMyProfileInfo', payload)


    async def is_exist_username(self, username: str) -> dict:
        payload: dict = {
            'username': username.split('@')[-1]
        }
        return await self.exequte('isExistUsername', payload)


    async def get_my_archive_stories(
            self,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False,
            profile_id: int = None,
    ) -> dict:
        payload: dict = {
            'limit': limit,
            'sort': sort,
            'equal': equal,
            'profile_id': profile_id,
        }
        return await self.exequte('getMyArchiveStories', payload)


    async def get_post_by_share_link(self, share_link: str) -> dict:
        payload: dict = {
            'share_link': share_link.split('/')[-1],
            'profile_id': None
        }
        return await self.exequte('getPostByShareLink', payload)


    async def get_profile_info(self, profile_id: int) -> dict:
        payload: dict = {
            'profile_id': None,
            'target_profile_id': profile_id
        }
        return await self.exequte('getProfileInfo', payload)


    async def follow(self, followee_id: int, profile_id: int = None) -> dict:
        payload: dict = {
            'f_type': 'Follw',
            'followee_id': followee_id,
            'profile_id': profile_id
        }
        return await self.exequte('requestFollow', payload)


    async def un_follow(self, followee_id: int, profile_id: int = None) -> dict:
        payload: dict = {
            'f_type': 'Unfollow',
            'followee_id': followee_id,
            'profile_id': profile_id
        }
        return await self.exequte('requestFollow', payload)


    async def create_page(self, **kwargs) -> dict:
        '''create_page(
            bio='',
            name='',
            username='',
            email='',
            phone='',
            website=''
            )'''
        payload: dict = {
            **kwargs
        }
        return await self.exequte('createPage', payload)


    async def remove_page(self, profile_id: int, record_id: int) -> dict:
        payload: dict = {
            'model': 'Profile',
            'record_id': record_id,
            'profile_id': profile_id
        }
        return await self.exequte('removeRecord', payload)


    async def update_profile(self, **kwargs) -> dict:
        '''update_profile(
            bio='',
            name='',
            username='',
            email='',
            phone='',
            website='',
            is_message_allowed=True or False,
            is_mute=True or False,
            profile_status='Public' or 'Private'
            )'''
        payload: dict = {
            **kwargs
        }
        return await self.exequte('updateProfile', payload)


    async def add_comment(
            self,
            text: str,
            post_id: int,
            target_profile_id: int,
            profile_id: int = None
    ) -> dict:
        payload: dict = {
            'content': text,
            'post_id': post_id,
            'post_profile_id': target_profile_id,
            'rnd': randint(1, 9),
            'profile_id': profile_id
        }
        return await self.exequte('addComment', payload)


    async def like(self, post_id: int, target_profile_id: int, profile_id: int = None) -> dict:
        payload: dict = {
            'action_type': 'Like',
            'post_id': post_id,
            'post_profile_id': target_profile_id,
            'profile_id': profile_id
        }
        return await self.exequte('likePostAction', payload)


    async def un_like(self, post_id: int, target_profile_id: int, profile_id: int = None) -> dict:
        payload: dict = {
            'action_type': 'Unlike',
            'post_id': post_id,
            'post_profile_id': target_profile_id,
            'profile_id': profile_id
        }
        return await self.exequte('likePostAction', payload)


    async def view(self, post_id: int, target_profile_id: int) -> dict:
        payload: dict = {
            'post_id': post_id,
            'post_profile_id': target_profile_id
        }
        return await self.exequte('addPostViewCount', payload)


    async def get_comments(
            self,
            post_id: int,
            target_profile_id: int,
            profile_id: int = None,
            sort: str = 'FromMax',
            limit : int = 20,
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'post_id': post_id,
            'post_profile_id': target_profile_id,
            'profile_id': profile_id,
            'sort': sort,
            'limit': limit,
            'equal': equal
        }
        return await self.exequte('getComments', payload)


    async def get_profile_posts(
            self,
            target_profile_id: int,
            profile_id: int = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'target_profile_id': target_profile_id,
            'profile_id': profile_id,
            'limit': limit,
            'sort': sort,
            'equal': equal,
        }
        return await self.exequte('getProfilePosts', payload)


    async def get_profiles_stories(self, profile_id: int, limit: int = 50) -> dict:
        payload: dict = {
            'limit': limit,
            'profile_id': profile_id
        }
        return await self.exequte('getProfilesStories', payload)


    async def get_recent_following_posts(
            self,
            profile_id: int = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'profile_id': profile_id,
            'limit': limit,
            'sort': sort,
            'equal': equal,
        }
        return await self.exequte('getRecentFollowingPosts', payload)


    async def get_bookmarked_posts(
            self,
            profile_id: int = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'profile_id': profile_id,
            'limit': limit,
            'sort': sort,
            'equal': equal
        }
        return await self.exequte('getBookmarkedPosts', payload)


    async def get_explore_posts(
            self,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False,
            max_id: str = None
    ) -> dict:
        payload: dict = {
            'profile_id': None,
            'limit': limit,
            'sort': sort,
            'equal': equal,
            'max_id': max_id,
        }
        return await self.exequte('getExplorePosts', payload)


    async def get_blocked_profiles(
            self,
            profile_id: int = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'profile_id': profile_id,
            'limit': limit,
            'sort': sort,
            'equal': equal
        }
        return await self.exequte('getBlockedProfiles', payload)


    async def get_profile_followers(
            self,
            target_profile_id: int,
            profile_id: int = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'target_profile_id': target_profile_id,
            'profile_id': profile_id,
            'limit': limit,
            'sort': sort,
            'equal': equal,
            'f_type': 'Follower',
        }
        return await self.exequte('getProfileFollowers', payload)


    async def get_profile_followings(
            self,
            target_profile_id: int,
            profile_id: int = None,
            limit: int = 50,
            sort: str = 'FromMax',
            equal: bool = False
    ) -> dict:
        payload: dict = {
            'target_profile_id': target_profile_id,
            'profile_id': profile_id,
            'limit': limit,
            'sort': sort,
            'equal': equal,
            'f_type': 'Following',
        }
        return await self.exequte('getProfileFollowers', payload)


    async def block_profile(self, blocked_id: int, profile_id: int = None) -> dict:
        payload: dict = {
            'action': 'Block',
            'blocked_id': blocked_id,
            'profile_id': profile_id
        }
        return await self.exequte('setBlockProfile', payload)


    async def un_block_profile(self, blocked_id: int, profile_id: int = None) -> dict:
        payload: dict = {
            'action': 'Unblock',
            'blocked_id': blocked_id,
            'profile_id': profile_id
        }
        return await self.exequte('setBlockProfile', payload)


    async def request_upload_file(
            self,
            file_name: str,
            file_size: int,
            file_type: str = 'Picture',
            profile_id: int = None
    ) -> dict:
        '''This method is a prerequisite for the `add_post` method'''
        payload: dict = {
            'file_name': file_name.split('/')[-1],
            'file_size': file_size,
            'file_type': file_type,
            'profile_id': profile_id
        }
        return await self.exequte('requestUploadFile', payload)


    async def upload_file(self, file: str, file_type: str = 'Picture', profile_id: int = None) -> dict:
        '''This method is a prerequisite for the `add_post` method'''
        filename, filesize = file.split('/')[-1], getsize(file)
        results = await self.request_upload_file(filename, filesize, file_type, profile_id)
        byte_file = open(file, 'rb').read()
        headers: dict = {
            'auth': self.auth,
            'file-id': results['data']['file_id'],
            'chunk-size': str(len(byte_file)),
            'total-part': '1',
            'part-number': '1',
            'hash-file-request': results['data']['hash_file_request']
        }
        return self.session.post(
            results['data']['server_url'], data=byte_file, headers=headers).json()['data'], results['data']


    async def add_post(
            self,
            file: str,
            caption: str = None,
            file_type: str = 'Picture',
            width: int = 720,
            height: int = 720,
            profile_id: int = None
    ) -> dict:
        results = await self.upload_file(file, file_type, profile_id)
        payload: dict = {
            'rnd': int(randint(0, 9)),
            'width': width,
            'height': height,
            'caption': caption,
            'file_id': results[1]['file_id'],
            'post_type': file_type,
            'profile_id': profile_id,
            'hash_file_receive': results[0]['hash_file_receive'],
            'thumbnail_file_id': results[1]['file_id'],
            'thumbnail_hash_file_receive': results[0]['hash_file_receive'],
            'is_multi_file': False
        }
        return await self.exequte('addPost', payload)
