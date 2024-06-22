import json


class Results:

    def __str__(self) -> str:
        return self.jsonify(indent=2)

    def __getattr__(self, name):
        return self.find_keys(keys=name)

    def __setitem__(self, key, value):
        self.original_update[key] = value

    def __getitem__(self, key):
        return self.original_update[key]

    def __lts__(self, update: list, *args, **kwargs):
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)
            elif isinstance(element, dict):
                update[index] = Results(update=element)
            else:
                update[index] = element

        return update

    def __init__(self, update: dict, *args, **kwargs) -> None:
        self.client = update.get('client')
        self.original_update = update

    def jsonify(self, indent=None) -> str:
        result = self.original_update
        result['original_update'] = 'dict{...}'
        return json.dumps(result, indent=indent, ensure_ascii=False, default=lambda value: str(value))

    def find_keys(self, keys, original_update=None, *args, **kwargs):
        if original_update is None:
            original_update = self.original_update

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(original_update, dict):
            for key in keys:
                try:
                    update = original_update[key]
                    if isinstance(update, dict):
                        update = Results(update=update)
                    elif isinstance(update, list):
                        update = self.__lts__(update=update)
                    return update
                except KeyError:
                    pass

            original_update = original_update.values()

        for value in original_update:
            if isinstance(value, (dict, list)):
                try:
                    return self.find_keys(keys=keys, original_update=value)
                except AttributeError:
                    return None

        return None

    @property
    def to_dict(self) -> dict:
        """
        Return the update as dict
        """
        return self.original_update

    @property
    def data(self):
        return self.find_keys("data")

    @property
    def profile(self):
        return self.data.find_keys("profile")

    @property
    def id(self):
        return self.profile.find_keys("id")

    @property
    def bio(self):
        return self.profile.find_keys("bio")

    @property
    def name(self):
        return self.profile.find_keys("name")

    @property
    def username(self):
        return self.profile.find_keys("username")

    @property
    def profile_status(self):
        return self.profile.find_keys("profile_status")

    @property
    def full_photo_url(self):
        return self.profile.find_keys("full_photo_url")

    @property
    def full_thumbnail_url(self):
        return self.profile.find_keys("full_thumbnail_url")

    @property
    def create_date(self):
        return self.profile.find_keys("create_date")

    @property
    def follower_count(self):
        return self.profile.find_keys("follower_count")

    @property
    def following_count(self):
        return self.profile.find_keys("following_count")

    @property
    def post_count(self):
        return self.profile.find_keys("post_count")

    @property
    def email(self):
        return self.profile.find_keys("email")

    @property
    def new_follow_request_count(self):
        return self.profile.find_keys("new_follow_request_count")

    @property
    def new_follow_request_count(self):
        return self.profile.find_keys("new_follow_request_count")

    @property
    def new_general_count(self):
        return self.profile.find_keys("new_general_count")

    @property
    def is_mute(self):
        return self.profile.find_keys("is_mute")

    @property
    def is_message_allowed(self):
        return self.profile.find_keys("is_message_allowed")

    @property
    def is_verified(self):
        return self.profile.find_keys("is_verified")

    @property
    def phone(self):
        return self.profile.find_keys("phone")

    @property
    def website(self):
        return self.profile.find_keys("website")

    @property
    def count_sale_unread(self):
        return self.profile.find_keys("count_sale_unread")

    @property
    def count_purchase(self):
        return self.profile.find_keys("count_purchase")

    @property
    def sale_permission(self):
        return self.profile.find_keys("sale_permission")

    @property
    def is_default(self):
        return self.profile.find_keys("is_default")

    @property
    def chat_link(self):
        return self.profile.find_keys("chat_link")

    @property
    def type(self):
        return self.chat_link.find_keys("type")

    @property
    def open_chat_data(self):
        return self.chat_link.find_keys("open_chat_data")

    @property
    def object_type(self):
        return self.open_chat_data.find_keys("object_type")

    @property
    def object_guid(self):
        return self.open_chat_data.find_keys("object_guid")

    @property
    def store_id(self):
        return self.profile.find_keys("store_id")

    @property
    def tag_post(self):
        return self.profile.find_keys("tag_post")

    @property
    def is_top_store(self):
        return self.profile.find_keys("is_top_store")

    @property
    def has_profile_link_item(self):
        return self.data.find_keys("has_profile_link_item")
