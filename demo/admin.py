from django.contrib import admin

from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    fields = ['title', 'image']


admin.site.register(Picture, PictureAdmin)
