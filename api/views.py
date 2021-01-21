from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse,HttpResponseBadRequest

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HistorySerializer
from .models import History
from .serializers import BookmarkSerializer
from .models import Bookmark

class HistoryView(APIView):
    # Get history
    def get(self, request, *args, **kwargs):
        query_set = History.objects.all()
        serializer = HistorySerializer(query_set, many=True)
        return Response(serializer.data)

    # Post history
    def post(self, request, *args, **kwargs):
        serializer = HistorySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return HttpResponseBadRequest(serializer.errors)

class BookmarkView(APIView):
    # Get Bookmark
    def get(self, request, *args, **kwargs):
        query_set = Bookmark.objects.all()
        serializer = BookmarkSerializer(query_set, many=True)
        return Response(serializer.data)

    # Post Bookmark
    def post(self, request, *args, **kwargs):
        serializer = BookmarkSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return HttpResponseBadRequest(serializer.errors)

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Bookmark, url=request.data["url"])
        instance.delete()
        return Response(status=200)
