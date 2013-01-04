from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

#helper method
def generate_link(image):
    return u"<a href='%s' target='_blank'>%s</a>" % (image.url, image.url.split('/')[-1])
    

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='originals')

    included = models.BooleanField(help_text="Check if the image should be included in PMH")
    title = models.CharField(max_length=100, blank=True, null=True, help_text="The image's title")

    caption = models.TextField(blank=True)

    terms = models.CharField(max_length=200, blank=True, help_text="A comma separated list of terms this image belongs to.")
    
    #The alternate sizes of the images
    medium_thumb = ImageSpecField([ResizeToFit(width=300, height=400)], image_field='image', cache_to='medium_thumbs')
    thumbnail = ImageSpecField([ResizeToFill(130, 130)], image_field='image', cache_to='thumbnails')

    def img_thumb(self):
        if self.image:
            #this is hacky, need to reverse lookup the image
            return u'<a href="%s/"><img src="%s" /></a>' % (self.id, self.thumbnail.url)
        else:
            return u'(No image)'

    img_thumb.short_description = 'Thumbnail'
    img_thumb.allow_tags = True

    def orig_filename(self):
        return generate_link(self.image)

    orig_filename.short_description = "Original"
    orig_filename.allow_tags = True

    def med_url(self):
        return generate_link(self.medium_thumb) 
    
    med_url.short_description = "Medium"
    med_url.allow_tags = True

    def __unicode__(self):
        return u"%s" % self.image.url.split('/')[-1]

    class Meta:
        ordering = ['-included']
