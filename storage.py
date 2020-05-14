import json

import settings


class AbstractStorage:
    async def get_comments_for_user_by_name(self, user_name: str, offset: int, limit: int):
        pass


class MockStorage(AbstractStorage):
    """
    Do NOT use in prod, it doesn't check path given by user at all!
    """

    async def get_comments_for_user_by_name(self, user_name: str, offset: int, limit: int):
        user_name = user_name.lower()

        if limit <= 0 or limit > settings.maximum_number_of_items_per_page:
            raise ValueError(f"limit '{limit}' is too big or 0")
        if offset < 0:
            raise ValueError("offset should be positive or 0")

        with open(f"./mock_data/{user_name}.json") as data:
            json_data = json.loads(data.read())
            return json_data[offset:offset + limit]


# DB Structure:
'''
 pikabu_id                     | bigint  |           | not null | nextval('pikabu_comments_pikabu_id_seq'::regclass) | plain    |              | 
 parent_id                     | bigint  |           | not null |                                                    | plain    |              | 
 created_at_timestamp          | bigint  |           | not null |                                                    | plain    |              | 
 text                          | text    |           | not null |                                                    | extended |              | 
 images                        | jsonb   |           | not null |                                                    | extended |              | 
 rating                        | integer |           | not null |                                                    | plain    |              | 
 number_of_pluses              | integer |           | not null |                                                    | plain    |              | 
 number_of_minuses             | integer |           | not null |                                                    | plain    |              | 
 story_id                      | bigint  |           | not null |                                                    | plain    |              | 
 story_url                     | text    |           | not null |                                                    | extended |              | 
 story_title                   | text    |           | not null |                                                    | extended |              | 
 author_id                     | bigint  |           | not null |                                                    | plain    |              | 
 author_username               | text    |           | not null |                                                    | extended |              | 
 author_gender                 | integer |           | not null |                                                    | plain    |              | 
 author_avatar_url             | text    |           | not null |                                                    | extended |              | 
 is_author_profile_deleted     | boolean |           | not null |                                                    | plain    |              | 
 is_deleted                    | boolean |           | not null |                                                    | plain    |              | 
 is_author_community_moderator | boolean |           | not null |                                                    | plain    |              | 
 is_author_pikabu_team         | boolean |           | not null |                                                    | plain    |              | 
 is_author_official            | boolean |           | not null |                                                    | plain    |              | 
 is_rating_hidden              | boolean |           | not null | false                                              | plain    |              | 
 ignore_code                   | integer |           | not null | 0                                                  | plain    |              | 
 is_ignored_by_someone         | boolean |           | not null | false                                              | plain    |              | 
 ignored_by                    | jsonb   |           | not null | '{}'::jsonb                                        | extended |              | 
'''
