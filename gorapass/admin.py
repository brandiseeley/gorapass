from django.contrib import admin

from .models import Stamps, Hikes, CompletedHikes, CompletedStamps

admin.site.register(Stamps)
admin.site.register(Hikes)
admin.site.register(CompletedHikes)
admin.site.register(CompletedStamps)
