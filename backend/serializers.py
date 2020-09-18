from rest_framework import serializers
# Models
from blog.models import *


class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.StringRelatedField(source='author.username', read_only=True)
    date_posted = serializers.DateTimeField(format="%Y:%m:%d")

    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'author_name', 'date_posted')