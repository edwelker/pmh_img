from django.contrib import admin
from images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('new_filename', 'img_thumb', 'terms', 'orig_filename', 'med_url', 'included')
    list_display_links = ('img_thumb',)
    list_editable = ('included', 'terms')
    search_fields = ('new_filename', 'orig_filename', 'terms')
    list_filter = ('included',)


admin.site.register(Image, ImageAdmin)
admin.site.disable_action('delete_selected')
