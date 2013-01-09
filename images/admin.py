from django.contrib import admin
from images.models import Image, TopicPage

class TopicPageInline(admin.TabularInline):
    model = TopicPage 
    extra = 3
    can_delete = False

class ImageAdmin(admin.ModelAdmin):
    list_display = ('included', 'img_thumb', 'name', 'orig_filename', 'med_url', 'complete')
    list_display_links = ('img_thumb', 'name', 'complete')
    list_editable = ('included',)
    list_per_page = 10
    search_fields = ('orig_filename',)
    list_filter = ('included',)

    #fieldsets = [
    #    (None, {'fields': ['image', 'included']}),
    #    ('Metadata', {'fields': ['orig_figure_source', 'pmh_figure_source', 'source_url', 'alt_text', 'caption']})
    #]
    inlines = [TopicPageInline]


admin.site.register(Image, ImageAdmin)
admin.site.disable_action('delete_selected')
