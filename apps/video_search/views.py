from apps.video_search.models import VideoProject
from apps.video_search.search import TsdVimeoClient, TsdYoutubeClient
from apps.video_search.serializers import VideoProjectSerializer, SearchVideoSerializer
from common.views import CommonGenericView, JsonResponse


class VideoProjectApi(CommonGenericView):
    serializer_class = VideoProjectSerializer

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

    def make_output_data(self, vimeo_data, yt_data):
        data_out = {
            'results': []
        }
        for item in vimeo_data.get('data',[]):
            data_out['results'].append(
                {'link': item['link']}
            )

        return data_out

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        search_text = validated_data['search_text']
        project_id = self.kwargs['id']
        vimeo_client = TsdVimeoClient()
        vimeo_result = vimeo_client.search({'query': search_text})
        # yt_client = TsdYoutubeClient()
        # result = yt_client.search('cats')
        data_out = self.make_output_data(vimeo_result, None)
        print(data_out)
        return JsonResponse(data_out)
