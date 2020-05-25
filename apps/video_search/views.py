from rest_framework.pagination import PageNumberPagination

from apps.video_search.models import VideoProject, VideoSearchResult
from apps.video_search.search import TsdVimeoClient, TsdYoutubeClient
from apps.video_search.serializers import VideoProjectSerializer, SearchVideoSerializer, SearchVideoResultsSerializer
from common.views import CommonGenericView, JsonResponse


class VideoProjectApi(CommonGenericView):
    serializer_class = VideoProjectSerializer
    pagination_class = None

    def get_queryset(self):
        return VideoProject.objects.filter()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SearchVideoApi(CommonGenericView):
    serializer_class = SearchVideoSerializer
    lookup_field = 'project_id'

    def make_output_data(self, vimeo_data, yt_data):
        data_out = {
            'results': []
        }
        for item in vimeo_data.get('data',[]):
            data_out['results'].append(
                {'link': item['link']}
            )

        return data_out

    def save_data_to_db(self, project_id, vimeo_data, yt_data):
        # delete previous results
        VideoSearchResult.objects.filter(project_id=project_id).delete()

        for item in vimeo_data.get('data',[]):
            VideoSearchResult.objects.create(
                project_id=project_id,
                source_link = item['link']
            )

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        search_text = validated_data['search_text']
        project_id = self.kwargs['project_id']
        vimeo_client = TsdVimeoClient()
        vimeo_result = vimeo_client.search({'query': search_text})
        # yt_client = TsdYoutubeClient()
        # result = yt_client.search('cats')
        #data_out = self.make_output_data(vimeo_result, None)
        self.save_data_to_db(project_id, vimeo_result, None)
        data_out = {}
        print(data_out)
        return JsonResponse(data_out)

class SearchVideoResultsApi(CommonGenericView):
    lookup_field = 'project_id'
    serializer_class = SearchVideoResultsSerializer

    def get_queryset(self):
        return VideoSearchResult.objects.filter(project_id=self.kwargs['project_id'])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

