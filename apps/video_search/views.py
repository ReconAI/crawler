from apps.video_search.models import VideoProject, VideoSearchResult
from apps.video_search.search import TsdVimeoClient, TsdYoutubeClient
from apps.video_search.serializers import VideoProjectSerializer, SearchVideoSerializer, SearchVideoResultsSerializer, \
    SearchVideoResultStatusSerializer
from common.views import CommonGenericView, JsonResponse
from apps.video_search.tasks import task_save_source_video_and_create_preview


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

        # async saving
        for item in vimeo_data.get('data',[]):
            link = item['link']
            video_title = item['name']
            video_search_result = VideoSearchResult.objects.create(
                project_id=project_id,
                source_link=link,
                video_title=video_title
            )
            task_save_source_video_and_create_preview.apply_async(kwargs={
                'video_search_result_id': video_search_result.id,
            })

        for item in yt_data.get('items', []):
            video_id = item['id'].get('videoId')
            video_title = item.get('snippet', {}).get('title','')
            if video_id is None:
                continue
            link = 'https://www.youtube.com/watch?v=%s' % video_id

            video_search_result = VideoSearchResult.objects.create(
                project_id=project_id,
                source_link=link,
                video_title=video_title,
            )
            task_save_source_video_and_create_preview.apply_async(kwargs={
                'video_search_result_id': video_search_result.id,
            })

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        search_text = validated_data['search_text']
        project_id = self.kwargs['project_id']
        vimeo_client = TsdVimeoClient()
        vimeo_result = vimeo_client.search({'query': search_text})
        yt_client = TsdYoutubeClient()
        yt_result = yt_client.search(search_text)
        #data_out = self.make_output_data(vimeo_result, None)
        self.save_data_to_db(project_id, vimeo_result, yt_result)
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


class SearchVideoResultStatusApi(CommonGenericView):
    lookup_field = 'id'
    serializer_class = SearchVideoResultStatusSerializer

    def get_queryset(self):
        return VideoSearchResult.objects.filter()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

