from django.contrib import admin
from images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('new_filename', 'image', 'img_thumb')
    search_fields = ('new_filename', 'image')

admin.site.register(Image, ImageAdmin)
