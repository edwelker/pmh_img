from django.contrib import admin
from images.models import Image, TopicPage
from django.forms import Textarea
from django.db import models

class TopicPageInline(admin.TabularInline):
    model = TopicPage 
    extra = 3
    can_delete = False

class ImageAdmin(admin.ModelAdmin):
    list_display = ('included', 'name', 'img_thumb', 'orig_filename', 'med_url', 'complete')
    list_display_links = ('img_thumb', 'complete')
    list_editable = ('included', 'name')
    list_per_page = 10
    search_fields = ('image', 'name', 'caption', 'alt_text')
    list_filter = ('included',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    fieldsets = [
        (None, {'fields': ['image', 'included']}),
        ('Metadata', {'fields': ['name', 'alt_text', 'caption', 'source_url', 'orig_figure_source', 'pmh_figure_source']})
    ]
    inlines = [TopicPageInline]


admin.site.register(Image, ImageAdmin)
admin.site.disable_action('delete_selected')
