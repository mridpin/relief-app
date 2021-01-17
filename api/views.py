from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class VideoView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "text": "Hello, World!",
        }
        return Response(data)
