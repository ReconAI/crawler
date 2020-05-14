from rest_framework import serializers

from apps.video_search.models import VideoProject
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
