import logging
import copy
from googleapiclient.discovery import build
from django.conf import settings
import vimeo

logger = logging.getLogger(__name__)


class TsdVimeoClient:
    client = None

    def __init__(self):
        self.default_params = {
            'per_page': settings.SEARCH_VIMEO_AMOUNT
        }
        self.client = vimeo.VimeoClient(
            token=settings.VIMEO_ACCESS_TOKEN,
            key=settings.VIMEO_CLIENT_ID,
            secret=settings.VIMEO_CLIENT_SECRET
        )

    def search(self, vimeo_params):
        """
        https://developer.vimeo.com/api/reference/videos#search_videos
        :param vimeo_params: are "query", "per_page",...
        :return:
        """
        params = copy.deepcopy(self.default_params)
        params.update(vimeo_params)

        response = self.client.get('/videos', params=params)

        if response.status_code == 200:
            return response.json()
        else:
            logger.warning('Bad response. Status code = %s' % response.status_code)


class TsdYoutubeClient:
    client = None
    default_params = {
    }

    def __init__(self):
        self.client = build(settings.YOUTUBE_API_SERVICE_NAME, settings.YOUTUBE_API_VERSION, developerKey=settings.YOUTUBE_API_DEVELOPER_KEY)

    def search(self, search_text):
        search_response = self.client.search().list(
            q=search_text,
            part='id,snippet',
            maxResults=settings.SEARCH_YOUTUBE_AMOUNT
        ).execute()
        return search_response
