import requests

from . import __version__
from .compat import json
from .exceptions import HuluError


class Hulu(object):
    def __init__(self):
        self.base_url = 'http://www.hulu.com/api/2.0/'

    def _request(self, endpoint, params):
        url = self.base_url + endpoint
        headers = {'User-Agent': 'Python Hulu v' + __version__}
        response = requests.get(url, params=params, headers=headers)
        try:
            content = json.loads(response.content.decode('utf8'))
        except ValueError:
            raise HuluError('Unable to decode response, not valid JSON.')

        return content

    def get(self, endpoint, **kwargs):
        return self._request(endpoint, params=kwargs)

    def get_companies(self, **kwargs):
        """Returns a list of companies that have shows/videos on Hulu"""
        return self.get('companies.json', **kwargs)

    def get_video_position_in_show(self, video_id, **kwargs):
        """Returns video position in list of videos from the show

        :param video_id: ID of the video you want to obtain the position of
        """
        kwargs['video_id'] = video_id
        return self.get('video_position_in_show', **kwargs)

    def get_videos(self, **kwargs):
        """Returns a list of videos"""
        return self.get('videos', **kwargs)

    def get_video_info(self, id, **kwargs):
        """Returns information about a specific video

        :param id: ID of the episode you want to obtain the position of
        """
        kwargs['id'] = id
        return self.get('info/video.json', **kwargs)

    def get_shows(self, **kwargs):
        """Returns list of shows available on Hulu"""
        return self.get('shows.json', **kwargs)

    def get_show_info(self, id, **kwargs):
        """Returns information about a specific show

        :param id: ID of the episode you want to obtain the position of
        """
        kwargs['id'] = id
        return self.get('info/show.json', **kwargs)

    def get_featured(self, **kwargs):
        """Returns featured content"""
        return self.get('featured.json', **kwargs)

    def get_video_games(self, **kwargs):
        """Returns a list of video games"""
        return self.get('video_games.json', **kwargs)

    def get_video_game(self, id, **kwargs):
        """Returns information about a specific video game

        :param id: ID of the episode you want to obtain the position of
        """
        kwargs['id'] = id
        return self.get('video_game.json', **kwargs)

    def get_criterions(self, **kwargs):
        """Return a list of criterions"""
        return self.get('criterions.json', **kwargs)

    def get_trailers(self, **kwargs):
        """Returns a list of trailers available on Hulu"""
        return self.get('trailers.json', **kwargs)
