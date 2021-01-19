from rest_framework import serializers
from .models import History
from .models import Bookmark

# History DTO
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = (
            "url",
        )

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = (
            "url",
        )        