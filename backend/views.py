from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from blog.models import *
from .serializers import *


def backend_home(request):
    return render(request, 'backend/backend_home.html')

@api_view(['GET'])
def api_post_list(request):

    data = Post.objects.all()
    serializer = PostSerializer(data, context={'request': request}, many=True)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def api_post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)