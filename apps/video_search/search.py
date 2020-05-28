import logging
import copy
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from crawler.settings import VIMEO_ACCESS_TOKEN, VIMEO_CLIENT_ID, VIMEO_CLIENT_SECRET, YOUTUBE_API_DEVELOPER_KEY, \
    YOUTUBE_API_VERSION, YOUTUBE_API_SERVICE_NAME
import vimeo

logger = logging.getLogger(__name__)


class TsdVimeoClient:
    client = None
    default_params = {
        'per_page': 1
    }

    def __init__(self):
        self.client = vimeo.VimeoClient(
            token=VIMEO_ACCESS_TOKEN,
            key=VIMEO_CLIENT_ID,
            secret=VIMEO_CLIENT_SECRET
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
        self.client = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_DEVELOPER_KEY)

    def search(self, search_text):
        search_response = self.client.search().list(
            q=search_text,
            part='id,snippet',
            maxResults=1
        ).execute()
        return search_response
