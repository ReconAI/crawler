from rest_framework import serializers

from apps.video_search.models import VideoProject, VideoSearchResult
from common.serializers import CommonSerializer


class VideoProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoProject
        fields = (
            'id',
            'name',
        )
        read_only_fields = ('id',)

class SearchVideoVimeoFiltersSerializer(CommonSerializer):
    video_license = serializers.CharField(source='license')

class SearchVideoYoutubeFiltersSerializer(CommonSerializer):
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    location_radius = serializers.IntegerField(required=False)

class SearchVideoSerializer(CommonSerializer):
    search_text = serializers.CharField()
    #vimeo_filters = SearchVideoVimeoFiltersSerializer()
    yt_filters = SearchVideoYoutubeFiltersSerializer()

class SearchVideoResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSearchResult
        fields = (
            'id',
            'source_link',
            'preview_link',
            'video_title',
            'published_at',
            'duration',
            'width',
            'height',
        )


class SearchVideoResultStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSearchResult
        fields = (
            'status',
        )
