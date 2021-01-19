from django.contrib import admin

from .models import History
from .models import Bookmark

# Register your models here.
admin.site.register(History)
admin.site.register(Bookmark)