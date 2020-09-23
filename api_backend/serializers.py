from rest_framework import serializers
from .models import MMANews


class MMANewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MMANews
        fields = ('article', 'title', 'thumbnail_url', 'img_url')