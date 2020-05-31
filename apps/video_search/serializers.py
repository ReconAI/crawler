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

class SearchVideoSerializer(CommonSerializer):
    search_text = serializers.CharField()


class SearchVideoResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSearchResult
        fields = (
            'id',
            'source_link',
            'preview_link',
            'video_title',
            'published_at',
        )


class SearchVideoResultStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSearchResult
        fields = (
            'status',
        )
