from apps.video_search.models import VideoProject
from apps.video_search.search import TsdVimeoClient
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

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        search_text = validated_data['search_text']
        project_id = self.kwargs['id']
        vimeo_client = TsdVimeoClient()
        result = vimeo_client.search({'query': search_text})
        print(result)

        data_out = {
            'result': 'test'
        }
        return JsonResponse(data_out)
