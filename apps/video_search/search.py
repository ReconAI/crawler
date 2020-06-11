import logging
import copy

import arrow
from googleapiclient.discovery import build
from django.conf import settings
import vimeo

logger = logging.getLogger(__name__)


class TsdVimeoClient:
    client = None

    def __init__(self, video_amount: int = None):
        self.default_params = {
            'per_page': video_amount if video_amount else settings.SEARCH_VIMEO_AMOUNT
        }
        self.client = vimeo.VimeoClient(
            token=settings.VIMEO_ACCESS_TOKEN,
            key=settings.VIMEO_CLIENT_ID,
            secret=settings.VIMEO_CLIENT_SECRET
        )

    def search(self, search_text:str, video_license=None, video_duration=None, minimum_likes=None):
        """
        https://developer.vimeo.com/api/reference/videos#search_videos
        :param vimeo_params: are "query", "per_page",...
        :return:
        """

        params = copy.deepcopy(self.default_params)
        params['query'] = search_text
        vimeo_filters = []
        if video_license:
            vimeo_filters.append(video_license) # strange Vimeo format for license
        if video_duration:
            vimeo_filters.append('duration')
            params['filter_duration'] = video_duration
        if minimum_likes:
            vimeo_filters.append('minimum_likes')
            params['filter_minimum_likes'] = minimum_likes

        # turn on filters
        params['params'] = ','.join(vimeo_filters)

        response = self.client.get('/videos', params=params)

        if response.status_code == 200:
            return response.json()
        else:
            logger.warning('Bad response. Status code = %s' % response.status_code)


class TsdYoutubeClient:
    client = None
    default_params = {
    }

    def __init__(self, video_amount: int = None):
        self.client = build(settings.YOUTUBE_API_SERVICE_NAME, settings.YOUTUBE_API_VERSION, developerKey=settings.YOUTUBE_API_DEVELOPER_KEY)
        self.video_amount = video_amount if video_amount else settings.SEARCH_YOUTUBE_AMOUNT

    def search(
            self, search_text: str, latitude: float = None, longitude: float = None, location_radius: int = None,
            published_before=None, published_after=None, safe_search=None, video_category_id:int=None, video_definition=None,
            video_duration=None, video_license=None
    ):
        params = dict(
            q=search_text,
            type='video',
            part='id,snippet',
            maxResults=self.video_amount
        )
        if latitude and longitude and location_radius:
            params['location'] = '%s,%s' % (latitude, longitude)
            params['locationRadius'] = '%skm' % location_radius
        if published_before:
            params['publishedBefore'] = arrow.get(published_before).isoformat()
        if published_after:
            params['publishedAfter'] = arrow.get(published_after).isoformat()
        if safe_search:
            params['safeSearch'] = safe_search
        if video_category_id:
            params['videoCategoryId'] = video_category_id
        if video_definition:
            params['videoDefinition'] = video_definition
        if video_duration:
            params['videoDuration'] = video_duration
        if video_license:
            params['videoLicense'] = video_license

        # execute request
        try:
            print('Params=%s' % params)
            search_response = self.client.search().list(**params).execute()
        except Exception as e:
            # add some code here
            raise
        return search_response
