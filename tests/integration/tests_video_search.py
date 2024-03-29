from django.test import override_settings

from apps.video_search.models import VideoProject, VideoSearchResult
from common.testing import CommonTestCase

from rest_framework import status as rest_status

from tests.integration.factories import VideoProjectFactory, VideoSearchResultFactory


class VideoProjectApiTestCase(CommonTestCase):

    def test_ok_create_video_project(self):
        data_in = {
            'name': 'test_name'
        }
        response = self.client.post('/api/video-project/', data=data_in)
        self.assertEqual(response.status_code, rest_status.HTTP_201_CREATED)
        print(response.content)
        self.assertEqual(VideoProject.objects.count(), 1)

    def test_ok_get_list(self):
        VideoProjectFactory.create(name='test1')
        VideoProjectFactory.create(name='test2')

        response = self.client.get('/api/video-project/')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        content_dict = self.content_to_dict(response.content)
        self.assertEqual(len(content_dict), 2)

    def test_ok_delete(self):
        VideoProjectFactory.create(name='test1')
        vp = VideoProjectFactory.create(name='test2')

        response = self.client.delete(f'/api/video-project/{vp.id}/')
        self.assertEqual(response.status_code, rest_status.HTTP_204_NO_CONTENT)
        self.assertEqual(VideoProject.objects.count(), 1)


class SearchVideoApiTestCase(CommonTestCase):

    @override_settings(SEARCH_YOUTUBE_AMOUNT=5, SEARCH_VIMEO_AMOUNT=5)
    def test_run_search(self):
        vp = VideoProjectFactory.create(name='test2')
        data_in = {
            'search_text': 'cats'
        }
        response = self.client.post(f'/api/video-project/{vp.id}/search/', data=data_in)
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        self.assertEqual(VideoSearchResult.objects.count(), 10)

    def test_show_search_result(self):
        vp = VideoProjectFactory.create(name='test2')
        VideoSearchResultFactory.create(project=vp, source_link='http://google.com')

        response = self.client.get(f'/api/video-project/{vp.id}/search/results/')
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        print(response.content)
        content_dict = self.content_to_dict(response.content)
        self.assertEqual(len(content_dict['results']), 1)

class SearchVideoResultStatusApiTestCase(CommonTestCase):

    def test_ok(self):
        vp = VideoProjectFactory.create(name='test2')
        vsr = VideoSearchResultFactory.create(project=vp, source_link='http://google.com')
        data_in = {
            'status': 'CONFIRMED'
        }
        response = self.client.put(f'/api/search-results/{vsr.id}/status/', data=data_in)
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)
        vsr = VideoSearchResult.objects.get()
        self.assertEqual(vsr.status, 'CONFIRMED')



