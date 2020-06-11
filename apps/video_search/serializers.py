from rest_framework import serializers

from apps.video_search.models import VideoProject, VideoSearchResult
from common.enum import ChoiceEnum
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
    video_license = serializers.CharField(required=False)
    video_duration = serializers.IntegerField(required=False)
    minimum_likes = serializers.IntegerField(required=False)
    trending = serializers.BooleanField(required=False)

class SafeSearchEnum(ChoiceEnum):
    STRICT = 'strict'
    MODERATE = 'moderate'
    NONE = 'none'


class VideoDefinitionEnum(ChoiceEnum):
    ANY = 'any'
    STANDARD = 'standard'
    HIGH = 'high'


class VideoDurationEnum(ChoiceEnum):
    SHORT = 'short'
    MEDIUM = 'medium'
    LONG = 'long'
    ANY = 'any'


class YoutubeVideoLicenseEnum(ChoiceEnum):
    YOUTUBE = 'youtube'
    CREATIVE_COMMON = 'creativeCommon'
    ANY = 'any'


class SearchVideoYoutubeFiltersSerializer(CommonSerializer):
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    location_radius = serializers.IntegerField(required=False)
    published_before = serializers.DateField(required=False)
    published_after = serializers.DateField(required=False)
    safe_search = serializers.ChoiceField(choices=SafeSearchEnum.for_choice(), required=False)
    video_category_id = serializers.IntegerField(required=False)
    video_definition = serializers.ChoiceField(choices=VideoDefinitionEnum.for_choice(), required=False)
    video_duration = serializers.ChoiceField(choices=VideoDurationEnum.for_choice(), required=False)
    video_license = serializers.ChoiceField(choices=YoutubeVideoLicenseEnum.for_choice(), required=False)

class SearchVideoSerializer(CommonSerializer):
    search_text = serializers.CharField()
    video_amount = serializers.IntegerField()
    vimeo_filters = SearchVideoVimeoFiltersSerializer()
    yt_filters = SearchVideoYoutubeFiltersSerializer()

class SearchVideoResultsSerializer(serializers.ModelSerializer):
    embedded_link = serializers.SerializerMethodField()

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
            'embedded_link'
        )
    def get_embedded_link(self, instance):
        if 'vimeo.com' in instance.source_link:
            video_part = instance.source_link.rsplit('/')[-1]
            embedded_link = 'https://player.vimeo.com/video/%s' % video_part
            return embedded_link
        else:
            video_part = instance.source_link.rsplit('https://www.youtube.com/watch?v=')[-1]
            embedded_link = 'https://www.youtube.com/embed/%s' % video_part
            return embedded_link



class SearchVideoResultStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSearchResult
        fields = (
            'status',
        )
