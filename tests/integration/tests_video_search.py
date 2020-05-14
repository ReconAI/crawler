from apps.video_search.models import VideoProject
from common.testing import CommonTestCase

from rest_framework import status as rest_status

from tests.integration.factories import VideoProjectFactory


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

        response = self.client.delete(f'/api/video-project/{vp.id}')
        self.assertEqual(response.status_code, rest_status.HTTP_204_NO_CONTENT)
        self.assertEqual(VideoProject.objects.count(), 1)


class SearchVideoApiTestCase(CommonTestCase):

    def test_ok_search(self):
        vp = VideoProjectFactory.create(name='test2')
        data_in = {
            'search_text': 'cats'
        }
        response = self.client.post(f'/api/video-project/{vp.id}/search/', data=data_in)
        self.assertEqual(response.status_code, rest_status.HTTP_200_OK)

