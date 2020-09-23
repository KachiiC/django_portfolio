from django.shortcuts import render

@api_view(['GET'])
def mma_news_list(request):
    if request.method == 'GET':
        mma_news = MMANews.objects.all()

        serializer = MMANewsSerializer(mma_news, context={'request': request}, many=True)

        return Response(serializer.data)
