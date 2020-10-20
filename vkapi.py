import vk_api
import random


def get_wall_posts(token, group_id):

    '''
    TODO
    1. Need to get more than 100 posts (wall.get limit). 100 is too little learning,
    especially after cleaning.
    2. The vk app token should be permanent. Research that.

    '''

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    posts = vk.wall.get(owner_id=group_id, count=100)
    res = []
    for i in posts['items']:
        res.append(i['text'])
    
    return res