from django.contrib import admin
from pmh_images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('new_filename', 'original_filename', 'img_thumb')
    search_fields = ('new_filename', 'original_filename')

admin.site.register(Image, ImageAdmin)
