import logging
import copy
from crawler.settings import VIMEO_ACCESS_TOKEN, VIMEO_CLIENT_ID, VIMEO_CLIENT_SECRET
import vimeo

logger = logging.getLogger(__name__)


class TsdVimeoClient:
    client = None
    default_params = {
        'per_page': 10
    }

    def __init__(self):
        self.client = vimeo.VimeoClient(
            token=VIMEO_ACCESS_TOKEN,
            key=VIMEO_CLIENT_ID,
            secret=VIMEO_CLIENT_SECRET
        )

    def search(self, vimeo_params):
        params = copy.deepcopy(self.default_params)
        params.update(vimeo_params)

        response = self.client.get('/videos', params=params)

        if response.status_code == 200:
            return response.json()
        else:
            logger.warning('Bad response. Status code = %s' % response.status_code)
