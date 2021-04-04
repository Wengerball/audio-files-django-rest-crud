from rest_framework import serializers
from audiofiles.models import Song, Podcast, Audiobook


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'
