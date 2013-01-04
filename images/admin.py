from django.contrib import admin
from images.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_thumb', 'terms', 'orig_filename', 'med_url', 'included')
    list_display_links = ('title', 'img_thumb',)
    list_editable = ('included', 'terms')
    search_fields = ('title', 'orig_filename', 'terms')
    list_filter = ('included',)


admin.site.register(Image, ImageAdmin)
admin.site.disable_action('delete_selected')
