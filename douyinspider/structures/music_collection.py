from douyinspider.structures import Base
from douyinspider.utils.fetch import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers


class MusicCollection(Base):
    
    def __init__(self, **kwargs):
        """
        music init args
        :param kwargs:
        """
        super().__init__()
        self.mc_id = kwargs.get('mc_id')
        self.mc_name = kwargs.get('mc_name')
        self.mc_musics = kwargs.get('mc_musics')
    
    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Music: <%s, %s>>' % (self.mc_id, self.mc_name)
    
    # def videos(self, max=None):
    #     """
    #     get videos of topic
    #     :return:
    #     """
    #     if max and not isinstance(max, int):
    #         raise RuntimeError('`max` param must be int')
    #     from douyinspider.utils.tranform import data_to_video
    #     query = {
    #         'device_id': '33333333',
    #         'music_id': self.id,
    #         'count': '18',
    #     }
    #     offset, count = 0, 0
    #     while True:
    #         # define cursor
    #         query['cursor'] = str(offset)
    #         result = fetch(URL.music2video_url, params=query, headers=common_headers, verify=False)
    #         aweme_list = result.get('aweme_list', [])
    #         for item in aweme_list:
    #             video = data_to_video(item)
    #             count += 1
    #             yield video
    #             if max and count >= max:
    #                 return
    #         # next page
    #         if result.get('has_more'):
    #             offset += 18
    #         else:
    #             break
