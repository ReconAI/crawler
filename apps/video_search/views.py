from apps.video_search.models import VideoProject
from apps.video_search.serializers import VideoProjectSerializer
from common.views import CommonGenericView


class VideoProjectApi(CommonGenericView):
    serializer_class = VideoProjectSerializer

    def get_queryset(self):
        return VideoProject.objects.filter()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
