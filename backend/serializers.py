from rest_framework import serializers
# Models
from blog.models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'date_posted')